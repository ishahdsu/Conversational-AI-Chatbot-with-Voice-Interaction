from flask import Flask, request, jsonify, render_template, session, send_from_directory
from flask_session import Session
import google.generativeai as genai

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

# Configure the Google Generative AI API
GOOGLE_API_KEY = 'MYGOOGLE_API_KEY'
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    session['conversation'] = []  # Initialize an empty conversation
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    # Retrieve conversation from session
    conversation = session.get('conversation', [])
    
    # Add user's message to the conversation history
    conversation.append(f"You: {user_message}")
    
    # Create input for AI model by joining conversation history
    conversation_input = "\n".join(conversation)
    
    response = model.generate_content(conversation_input)
    response.resolve()
    
    # Ensure the response does not contain duplicate "Bot: " at the beginning
    response_text = response.text
    if response_text.startswith("Bot: Bot:"):
        response_text = response_text.replace("Bot: Bot:", "Bot:", 1)
    
    # Add AI's response to the conversation history
    conversation.append(f"Bot: {response_text}")
    
    # Update the session with the new conversation history
    session['conversation'] = conversation
    
    return jsonify({'response': response_text})

if __name__ == '__main__':
    app.run(debug=True)
