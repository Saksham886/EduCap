from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from gtts import gTTS
from pymongo import MongoClient
from dotenv import load_dotenv
from transformers import pipeline, BartTokenizer, BartForConditionalGeneration
from youtube_transcript_api import YouTubeTranscriptApi
import PyPDF2
import os
import datetime
import re
import io
import torch
from newspaper import Article
from deep_translator import GoogleTranslator
from reportlab.pdfgen import canvas
from flask_jwt_extended import JWTManager, create_access_token, get_jwt_identity, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from vocamate_chatbot import vocamate_bp
# Load environment variables first
load_dotenv()

# Initialize Flask
app = Flask(__name__)
CORS(app, supports_credentials=True)

# JWT Configuration
jwt_secret = os.getenv("JWT_SECRET_KEY")
if not jwt_secret:
    raise ValueError("JWT_SECRET_KEY environment variable not set")
    
app.config["JWT_SECRET_KEY"] = jwt_secret
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(hours=24)
jwt = JWTManager(app)

# MongoDB Setup
mongo_uri = os.getenv("Local_mongo")
db_name = os.getenv("DB_NAME", "education_db")

try:
    client = MongoClient(mongo_uri)
    db = client[db_name]
    # Create TTL index on "timestamp" field (auto-expire documents after 24 hours)
    db.summaries.create_index(
        [("timestamp", 1)],
        expireAfterSeconds=86400  # 24 hours
    )
    print("✓ MongoDB connected successfully")
    print("✓ TTL index for 'summaries.timestamp' created (24h expiry)")
except Exception as e:
    print(f"⚠️ MongoDB connection error: {e}")
    raise

# Torch Device
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"✓ Using device: {device}")

# Load BART model
try:
    model_name = "facebook/bart-large-cnn"
    tokenizer = BartTokenizer.from_pretrained(model_name)
    model = BartForConditionalGeneration.from_pretrained(model_name).to(device)
    summarizer = pipeline(
        "summarization",
        model=model,
        tokenizer=tokenizer,
        device=0 if torch.cuda.is_available() else -1
    )
    print("✓ BART-Large-CNN model loaded successfully")
except Exception as e:
    print(f"⚠️ Error loading BART model: {e}")
    summarizer = None

# Helper Functions
def simple_summarizer(text):
    """Fallback summarizer when ML model fails"""
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    return '. '.join(sentences[:3]) + '.' if len(sentences) > 3 else text

def extract_video_id(url):
    """Extract YouTube video ID from URL"""
    regex = r"(?:youtube\.com\/(?:[^\/]+\/.+\/|(?:v|e(?:mbed)?)\/|.*[?&]v=)|youtu\.be\/)([^\"&?\/\s]{11})"
    match = re.search(regex, url)
    return match.group(1) if match else None

def get_youtube_transcript(video_id):
    """Get transcript from YouTube video"""
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([entry['text'] for entry in transcript])
    except Exception as e:
        print(f"Error fetching transcript: {e}")
        return None

def chunk_text(text, max_tokens=1000):
    """Split text into chunks of max_tokens"""
    words = text.split()
    chunks = [' '.join(words[i:i+max_tokens]) for i in range(0, len(words), max_tokens)]
    return chunks

def summarize_long_text(text):
    """Summarize text, handling long inputs by chunking"""
    if not text or len(text.strip()) == 0:
        return "No text provided for summarization."
        
    if not summarizer:
        return simple_summarizer(text)

    chunks = chunk_text(text)
    summaries = []

    for chunk in chunks:
        try:
            input_length = len(chunk.split())
            max_length = min(150, input_length // 2)
            min_length = min(30, max_length // 2)

            summary = summarizer(
                chunk,
                max_length=max_length,
                min_length=min_length,
                do_sample=False,
                truncation=True
            )[0]["summary_text"]
            summaries.append(summary)
        except Exception as e:
            print(f"Error summarizing chunk: {e}")
            summaries.append(simple_summarizer(chunk))

    return " ".join(summaries)

def extract_text_from_pdf(file):
    """Extract text content from PDF file"""
    try:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text() or ""
        return text
    except Exception as e:
        print(f"Error reading PDF: {e}")
        return None

def validate_url(url):
    """Basic URL validation"""
    url_pattern = re.compile(
        r'^(?:http|https)://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ipv4
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return bool(url_pattern.match(url))

def save_summary(user_id, original_text, summary, model_used, source):
    """Save summary to database if user is authenticated"""
    if user_id != "anonymous":
        try:
            db.summaries.insert_one({
                "user_id": user_id,
                "original_text": original_text[:500],  # Store only first 500 chars of original
                "summary": summary,
                "timestamp": datetime.datetime.now(),
                "model_used": model_used,
                "source": source
            })
            return True
        except Exception as e:
            print(f"Error saving summary: {e}")
    return False

# Routes
@app.route("/signup", methods=["POST"])
def signup():
    """Register a new user"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415
        
    data = request.get_json()
    email = data.get("email", "").strip()
    password = data.get("password", "")

    # Input validation
    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400
        
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        return jsonify({"error": "Invalid email format"}), 400
        
    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    try:
        if db.users.find_one({"email": email}):
            return jsonify({"error": "User already exists"}), 409

        hashed_password = generate_password_hash(password)
        db.users.insert_one({
            "email": email,
            "password": hashed_password,
            "created_at": datetime.datetime.now()
        })
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        return jsonify({"error": "Database error during registration"}), 500

@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return JWT token"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415
        
    data = request.get_json()
    email = data.get("email", "").strip()
    password = data.get("password", "")

    if not email or not password:
        return jsonify({"error": "Email and password required"}), 400

    try:
        user = db.users.find_one({"email": email})
        if not user or not check_password_hash(user["password"], password):
            return jsonify({"error": "Invalid credentials"}), 401

        token = create_access_token(identity=email)
        return jsonify({
            "token": token,
            "email": email
        })
    except Exception as e:
        return jsonify({"error": "Authentication error"}), 500

@app.route("/summarize", methods=["POST"])
def summarize_text():
    """Summarize text with optional translation"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    text = data.get("text", "").strip()
    input_lang = data.get("input_lang", "en")
    return_lang = data.get("return_lang", "en")

    if not text:
        return jsonify({"error": "Missing 'text' parameter"}), 400

    try:
        # Get user id from JWT if available
        try:
            current_user = get_jwt_identity()
        except:
            current_user = "anonymous"

        # Translate to English if needed
        if input_lang != "en":
            try:
                text = GoogleTranslator(source=input_lang, target="en").translate(text)
            except Exception as e:
                return jsonify({"error": f"Translation error: {str(e)}"}), 500

        # Summarize
        summary = summarize_long_text(text)
        model_used = "bart-large-cnn" if summarizer else "fallback"

        # Translate back if needed
        if return_lang != "en":
            try:
                summary = GoogleTranslator(source="en", target=return_lang).translate(summary)
            except Exception as e:
                return jsonify({"error": f"Translation error: {str(e)}"}), 500

        # Save summary if user is authenticated
        saved = save_summary(
            user_id=current_user,
            original_text=text,
            summary=summary,
            model_used=model_used,
            source="direct-input"
        )

        return jsonify({
            "summary": summary,
            "model": model_used,
            "saved": saved
        })

    except Exception as e:
        return jsonify({"error": f"Summarization error: {str(e)}"}), 500
import traceback
@app.route("/summarize_url", methods=["POST"])
def summarize_url():
    """Summarize content from URL"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    url = data.get("url", "").strip()

    if not url:
        return jsonify({"error": "Missing 'url' parameter"}), 400
        
    if not validate_url(url):
        return jsonify({"error": "Invalid URL format"}), 400

    try:
        # Get user id from JWT if available
        try:
            current_user = get_jwt_identity()
        except:
            current_user = "anonymous"
            
        # Extract article content
        article = Article(url)
        article.download()
        article.parse()
        text = article.text

        if not text:
            return jsonify({"error": "No text found in the article"}), 400

        # Summarize
        summary = summarize_long_text(text)
        model_used = "bart-large-cnn" if summarizer else "fallback"

        # Save summary if user is authenticated
        saved = save_summary(
            user_id=current_user,
            original_text=text,
            summary=summary,
            model_used=model_used,
            source=url
        )

        return jsonify({
            "summary": summary,
            "title": article.title,
            "model": model_used,
            "saved": saved
        })

    except Exception as e:
    
        traceback.print_exc()  # 👈 This shows the full traceback in your terminal
        return jsonify({"error": f"Failed to process URL: {str(e)}"}), 500


@app.route("/summarize_pdf", methods=["POST"])
def summarize_pdf():
    """Summarize content from PDF file"""
    file = request.files.get("file")
    
    # Get user id from JWT if available
    try:
        current_user = get_jwt_identity()
    except:
        current_user = "anonymous"

    if not file:
        return jsonify({"error": "No PDF uploaded"}), 400
        
    # Check if file is PDF
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Uploaded file must be a PDF"}), 400

    try:
        text = extract_text_from_pdf(file)
        if not text:
            return jsonify({"error": "Could not extract text from PDF"}), 500

        # Summarize
        summary = summarize_long_text(text)
        model_used = "bart-large-cnn" if summarizer else "fallback"

        # Save summary if user is authenticated
        saved = save_summary(
            user_id=current_user,
            original_text=text,
            summary=summary,
            model_used=model_used,
            source=f"pdf:{file.filename}"
        )

        return jsonify({
            "summary": summary,
            "model": model_used,
            "saved": saved
        })

    except Exception as e:
        return jsonify({"error": f"PDF processing error: {str(e)}"}), 500

@app.route("/summarize_youtube", methods=["POST"])
def summarize_youtube():
    """Summarize content from YouTube video transcript"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    url = data.get("url", "").strip()

    if not url:
        return jsonify({"error": "Missing YouTube URL"}), 400

    video_id = extract_video_id(url)
    if not video_id:
        return jsonify({"error": "Invalid YouTube URL"}), 400

    try:
        # Get user id from JWT if available
        try:
            current_user = get_jwt_identity()
        except:
            current_user = "anonymous"
            
        # Get transcript
        transcript = get_youtube_transcript(video_id)
        if not transcript:
            return jsonify({"error": "Could not fetch transcript. Video may not have captions."}), 500

        # Summarize
        summary = summarize_long_text(transcript)
        model_used = "bart-large-cnn" if summarizer else "fallback"

        # Save summary if user is authenticated
        saved = save_summary(
            user_id=current_user,
            original_text=transcript,
            summary=summary,
            model_used=model_used,
            source=f"youtube:{video_id}"
        )

        return jsonify({
            "summary": summary,
            "model": model_used,
            "saved": saved,
            "video_id": video_id
        })

    except Exception as e:
        return jsonify({"error": f"YouTube processing error: {str(e)}"}), 500

@app.route("/tts", methods=["POST"])
def text_to_speech():
    """Convert text to speech audio file"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415

    data = request.get_json()
    text = data.get("text", "").strip()
    lang = data.get("lang", "en")

    if not text:
        return jsonify({"error": "Missing 'text' parameter"}), 400
        
    # Limit text length to prevent abuse
    if len(text) > 5000:
        return jsonify({"error": "Text too long. Maximum 5000 characters allowed."}), 400

    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        buffer = io.BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)
        
        filename = f"summary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.mp3"
        return send_file(
            buffer, 
            mimetype="audio/mpeg", 
            as_attachment=True, 
            download_name=filename
        )
    except Exception as e:
        return jsonify({"error": f"Text-to-speech error: {str(e)}"}), 500

@app.route('/translate', methods=['POST'])
def translate():
    """Translate text between languages"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415
        
    data = request.get_json()
    text = data.get('text', '').strip()
    source_lang = data.get('source_lang', 'auto')
    target_lang = data.get('target_lang', 'en')

    if not text:
        return jsonify({'error': 'Text is required'}), 400
        
    # Limit text length to prevent abuse
    if len(text) > 5000:
        return jsonify({"error": "Text too long. Maximum 5000 characters allowed."}), 400

    try:
        translated_text = GoogleTranslator(source=source_lang, target=target_lang).translate(text)
        if not translated_text:
            return jsonify({'error': 'Translation failed'}), 500
            
        return jsonify({
            'translated_text': translated_text,
            'source_lang': source_lang,
            'target_lang': target_lang
        })
    except Exception as e:
        return jsonify({'error': f"Translation error: {str(e)}"}), 500

@app.route('/export/pdf', methods=['POST'])
def export_pdf():
    """Export summary to PDF document"""
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 415
        
    data = request.get_json()
    summary = data.get("summary", "").strip()
    title = data.get("title", "Summary")

    if not summary:
        return jsonify({"error": "Missing summary text"}), 400

    try:
        buffer = io.BytesIO()
        pdf = canvas.Canvas(buffer)
        
        # Add title
        pdf.setFont("Helvetica-Bold", 16)
        pdf.drawString(100, 800, title)
        
        # Add timestamp
        pdf.setFont("Helvetica", 10)
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        pdf.drawString(100, 780, f"Generated: {timestamp}")
        
        # Add summary text
        pdf.setFont("Helvetica", 12)
        y = 750
        lines = []
        for sentence in summary.split('. '):
            if sentence:
                lines.append(sentence.strip() + '.')
                
        for line in lines:
            if y < 50:
                pdf.showPage()
                y = 800
            pdf.drawString(100, y, line)
            y -= 20

        pdf.save()
        buffer.seek(0)

        filename = f"summary_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf"
        return send_file(
            buffer,
            mimetype='application/pdf',
            as_attachment=True,
            download_name=filename
        )
    except Exception as e:
        return jsonify({"error": f"PDF generation error: {str(e)}"}), 500

@app.route("/history", methods=["GET"])
@jwt_required()
def get_user_history():
    """Get summary history for authenticated user"""
    user_id = get_jwt_identity()
    
    try:
        records = list(db.summaries.find({"user_id": user_id}).sort("timestamp", -1))
        for record in records:
            record["_id"] = str(record["_id"])
            # Format timestamp for display
            if "timestamp" in record:
                record["timestamp"] = record["timestamp"].strftime("%Y-%m-%d %H:%M:%S")
                
        return jsonify({
            "user": user_id,
            "records": records,
            "count": len(records)
        })
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500
app.register_blueprint(vocamate_bp) 
@app.route("/health", methods=["GET"])
def health_check():
    """Simple health check endpoint"""
    return jsonify({
        "status": "ok",
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "model": "bart-large-cnn" if summarizer else "fallback"
    })

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    debug = os.getenv("FLASK_ENV") == "development"
    app.run(host="0.0.0.0", port=port, debug=debug)
    