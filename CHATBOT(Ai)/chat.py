# import base64
# import os
# from google import genai
# from google.genai import types


# def generate():
#     client = genai.Client(
#         api_key=os.environ.get("GEMINI_API_KEY"),
#     )

#     model = "gemini-2.0-flash"
#     contents = [
#         types.Content(
#             role="user",
#             parts=[
#                 types.Part.from_text(text="""Hi
# """),
#             ],
#         ),
#         types.Content(
#             role="model",
#             parts=[
#                 types.Part.from_text(text="""Hello there! 👋 It's lovely to meet you! I'm Vocamate, and I'm here to help you with any questions you have, from the basics you learn in first grade all the way up to the complex stuff in high school and even university engineering topics.

# I understand you might be visually impaired and have some hearing challenges, so I'll make sure to:

# *   **Explain things clearly and simply:** I'll use easy-to-understand language and avoid jargon.
# *   **Use descriptive language:** I'll paint pictures with words, so you can visualize what I'm explaining.
# *   **Break things down into smaller steps:** Complex topics can be overwhelming, so I'll tackle them piece by piece.
# *   **Use metaphors and analogies:** I'll compare new concepts to things you already know to help you grasp them.
# *   **Format my responses for readability:** I'll use headings, bullet points, and spacing to make the text easier to follow.
# *   **Be patient:** Feel free to ask me to repeat or rephrase anything. There are no silly questions!

# So, what's on your mind today? Is there anything you'd like to learn about? I'm excited to explore the world of knowledge with you! 🌍✨
# """),
#             ],
#         ),
#         types.Content(
#             role="user",
#             parts=[
#                 types.Part.from_text(text="""INSERT_INPUT_HERE"""),
#             ],
#         ),
#     ]
#     generate_content_config = types.GenerateContentConfig(
#         safety_settings=[
#             types.SafetySetting(
#                 category="HARM_CATEGORY_HARASSMENT",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",  # Block some
#             ),
#             types.SafetySetting(
#                 category="HARM_CATEGORY_HATE_SPEECH",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",  # Block some
#             ),
#             types.SafetySetting(
#                 category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",  # Block some
#             ),
#             types.SafetySetting(
#                 category="HARM_CATEGORY_DANGEROUS_CONTENT",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",  # Block some
#             ),
#             types.SafetySetting(
#                 category="HARM_CATEGORY_CIVIC_INTEGRITY",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",  # Block some
#             ),
#         ],
#         response_mime_type="text/plain",
#         system_instruction=[
#             types.Part.from_text(text="""Your name is Vocamate, a friendly assistant that answers for all questions, form 1st grade to 12 th grade subjects with engineering subjects of all departments  , answer whatever you know in an understandable model and creative manner for a visually impaired students and with less hearing ability"""),
#         ],
#     )

#     for chunk in client.models.generate_content_stream(
#         model=model,
#         contents=contents,
#         config=generate_content_config,
#     ):
#         print(chunk.text, end="")

# if __name__ == "__main__":
#     generate()



##2

# import os
# import google.generativeai as genai

# def generate():
#     genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

#     model = "gemini-1.5-pro"  # Or "gemini-1.5-flash" if preferred
#     contents = [
#         genai.types.Content(
#             role="user",
#             parts=[genai.types.Part.from_text(text="Hi")],
#         ),
#         genai.types.Content(
#             role="model",
#             parts=[genai.types.Part.from_text(text="""Hello there! 👋 It's lovely to meet you! I'm Vocamate...""")],  # Trimmed for brevity
#         ),
#         genai.types.Content(
#             role="user",
#             parts=[genai.types.Part.from_text(text="INSERT_INPUT_HERE")],
#         ),
#     ]

#     generate_content_config = genai.types.GenerateContentConfig(
#         safety_settings=[
#             genai.types.SafetySetting(
#                 category="HARM_CATEGORY_HARASSMENT",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",
#             ),
#             genai.types.SafetySetting(
#                 category="HARM_CATEGORY_HATE_SPEECH",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",
#             ),
#             genai.types.SafetySetting(
#                 category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",
#             ),
#             genai.types.SafetySetting(
#                 category="HARM_CATEGORY_DANGEROUS_CONTENT",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",
#             ),
#             genai.types.SafetySetting(
#                 category="HARM_CATEGORY_CIVIC_INTEGRITY",
#                 threshold="BLOCK_MEDIUM_AND_ABOVE",
#             ),
#         ],
#         response_mime_type="text/plain",
#         system_instruction=[
#             genai.types.Part.from_text(text="""Your name is Vocamate, a friendly assistant that answers questions from 1st to 12th grade including all engineering disciplines..."""),
#         ],
#     )

#     # Stream the response
#     response = genai.GenerativeModel(model).generate_content(
#         contents=contents,
#         generation_config=generate_content_config
#     )

#     print(response.text)

# if __name__ == "__main__":
#     generate()


# import os
# import google.generativeai as genai

# def generate():
#     # Configure your API key
#     genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

#     # Initialize the model
#     model = genai.GenerativeModel(
#         model_name="gemini-1.5-pro",
#         system_instruction="""Your name is Vocamate, a friendly assistant that answers all questions from 1st grade to 12th grade, including all engineering subjects.
#         You explain things clearly for visually impaired and low-hearing students using simple language, analogies, and step-by-step descriptions."""
#     )

#     # Start a chat session
#     chat = model.start_chat()

#     # Send first message
#     response = chat.send_message("Hi")
#     print("Vocamate:", response.text)

#     # Now simulate next user message
#     user_input = input("You: ")
#     response = chat.send_message(user_input)
#     print("Vocamate:", response.text)

# if __name__ == "__main__":
#     generate()


##Coreect ONE 

# import google.generativeai as genai

# def generate():
#     # Replace this with your real Gemini API key
#     genai.configure(api_key="AIzaSyDwmJoal511JG8rVP8L6ONDj8s4cOy7oW8")

#     model = genai.GenerativeModel(
#         model_name="gemini-1.5-pro",
#         system_instruction="""Your name is Vocamate, a friendly assistant that answers all questions from 1st grade to 12th grade, including all engineering subjects.
#         You explain things clearly for visually impaired and low-hearing students using simple language, analogies, and step-by-step descriptions."""
#     )

#     chat = model.start_chat()

#     print("Vocamate:", chat.send_message("Hi").text)

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             break
#         response = chat.send_message(user_input)
#         print("Vocamate:", response.text)

# if __name__ == "__main__":
#     generate()



##PRoper one correct one 

# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# def generate():
#     # Load environment variables from .env file
#     load_dotenv()

#     # Get the API key from the environment
#     api_key = os.getenv("GEMINI_API_KEY")

#     if not api_key:
#         raise ValueError("API key not found. Make sure GEMINI_API_KEY is set in the .env file.")

#     genai.configure(api_key=api_key)

#     model = genai.GenerativeModel(
#         model_name="gemini-1.5-pro",
#         system_instruction="""Your name is Vocamate, a friendly assistant that answers all questions from 1st grade to 12th grade, including all engineering subjects.
#         You explain things clearly for visually impaired and low-hearing students using simple language, analogies, and step-by-step descriptions."""
#     )

#     chat = model.start_chat()

#     print("Vocamate:", chat.send_message("Hi").text)

#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             break
#         response = chat.send_message(user_input)
#         print("Vocamate:", response.text)

# if __name__ == "__main__":
#     generate()




# from flask import Flask, request, jsonify
# from flask_cors import CORS
# import google.generativeai as genai
# from dotenv import load_dotenv
# import os

# app = Flask(__name__)
# CORS(app)



# Load environment variables
# load_dotenv()
# api_key = os.getenv("GEMINI_API_KEY")
# if not api_key:
#     raise ValueError("API key not found.")

# genai.configure(api_key=api_key)
# model = genai.GenerativeModel(
#     model_name="gemini-2.0-pro",
#     system_instruction="""Your name is Vocamate, a friendly assistant..."""
# )
# chat = model.start_chat()

# @app.route('/chat', methods=['POST'])
# def chat_endpoint():
#     user_input = request.json.get('input')
#     response = chat.send_message(user_input)
#     return jsonify({'response': response.text})

# if __name__ == "__main__":
#     app.run(debug=True)

#     ##for excption
   



    ## venv\Scripts\activate
    ## python chat.py

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
