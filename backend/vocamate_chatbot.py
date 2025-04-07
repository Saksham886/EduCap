from flask import Blueprint, request, jsonify
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found.")

# Configure Gemini model
genai.configure(api_key=api_key)

# Create model instance
model = genai.GenerativeModel(model_name="gemini-1.5-flash")


# Start chat without system_instruction
chat = model.start_chat(history=[])

# Send initial instruction manually
chat.send_message(
    """Your name is Vocamate, a friendly assistant that answers all questions from 1st grade to 12th grade, including all engineering subjects.
    You explain things clearly for visually impaired and low-hearing students using simple language, analogies, and step-by-step descriptions."""
)

# Create a Flask blueprint
vocamate_bp = Blueprint('vocamate_bp', __name__)

@vocamate_bp.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        user_input = request.json.get('input')
        if not user_input:
            return jsonify({'error': 'No input provided'}), 400
        response = chat.send_message(user_input)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
