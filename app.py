import os
import logging
from flask import Flask, render_template, request, jsonify, session
from flask_cors import CORS
from chatbot import generate_response

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Create the Flask app
app = Flask(__name__)
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key")  # Fallback for development
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    """Render the main chat interface"""
    # Initialize session if needed
    if 'chat_history' not in session:
        session['chat_history'] = []
    
    return render_template('index.html')

@app.route('/api/message', methods=['POST'])
def process_message():
    """Process incoming messages and return a response"""
    try:
        data = request.get_json()
        user_message = data.get('message', '').strip()
        
        if not user_message:
            return jsonify({'error': 'Message cannot be empty'}), 400
        
        # Get chat history or initialize if not present
        chat_history = session.get('chat_history', [])
        
        # Generate response
        bot_response = generate_response(user_message, chat_history)
        
        # Update chat history
        chat_history.append({
            'sender': 'user',
            'message': user_message
        })
        chat_history.append({
            'sender': 'bot',
            'message': bot_response
        })
        
        # Save updated history to session
        session['chat_history'] = chat_history
        
        return jsonify({
            'response': bot_response,
            'history': chat_history
        })
    
    except Exception as e:
        logging.error(f"Error processing message: {str(e)}")
        return jsonify({'error': 'Failed to process your message. Please try again.'}), 500

@app.route('/api/history', methods=['GET'])
def get_history():
    """Return the current chat history"""
    chat_history = session.get('chat_history', [])
    return jsonify({'history': chat_history})

@app.route('/api/reset', methods=['POST'])
def reset_chat():
    """Reset the chat history"""
    session['chat_history'] = []
    return jsonify({'message': 'Chat history reset successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
