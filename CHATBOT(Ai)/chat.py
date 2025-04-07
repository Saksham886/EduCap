
from flask import Flask, request, jsonify
from flask_cors import CORS 
import google.generativeai as genai
from dotenv import load_dotenv
import os

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # 

# Load environment variables
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("API key not found.")

# Configure generative AI model
genai.configure(api_key=api_key)
model = genai.GenerativeModel(
    model_name="gemini-1.5-pro",  # Use the correct model name; "2.0" may not be valid
    system_instruction="""Your name is Vocamate, a friendly assistant..."""
)
chat = model.start_chat()

# Define the chat endpoint
@app.route('/chat', methods=['POST'])
def chat_endpoint():
    try:
        user_input = request.json.get('input')
        if not user_input:
            return jsonify({'error': 'No input provided'}), 400
        
        response = chat.send_message(user_input)
        return jsonify({'response': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Optional: Add a root route for quick testing
@app.route('/')
def home():
    return 'Vocamate backend is running!'

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
