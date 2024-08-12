# Conversational-AI-Chatbot-with-Voice-Interaction

This task demonstrates a web-based chatbot application that integrates text and voice interaction capabilities. Using a combination of frontend and backend technologies, the chatbot allows users to interact via text input or voice commands and responds with both text and speech. The AI model used for generating responses is Google’s Gemini-pro model, accessed through the Google Generative AI API.

## File Descriptions

### `app.py`
This is the backend server implemented using Flask. It handles the initialization of the application, manages user sessions, processes text input from the frontend, interacts with the AI model to generate responses, and manages the conversation history.

### `templates/index.html`
This is the frontend of the application. It provides the user interface for interacting with the chatbot. It includes the chat interface where users can type messages or record voice inputs. The voice input is processed using the Web Speech API for speech-to-text conversion, and the bot’s responses are converted to speech using the SpeechSynthesis interface.


