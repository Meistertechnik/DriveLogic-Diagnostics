# Flask Chatbot

A simple but feature-rich chatbot built with Flask and vanilla JavaScript.

## Features

- Text-based conversation with rule-based responses
- Jokes and fun facts
- Current date and time information
- Chat history with session management
- Responsive design with Bootstrap

## Getting Started

To run the application, simply use:

```bash
python main.py
```

Or for production environments, use Gunicorn:

```bash
./start_chatbot.sh
```

## Usage

The chatbot responds to various inputs:

- Greetings: "Hello", "Hi", "Hey"
- Questions: "What time is it?", "Tell me a joke"
- Commands: "Tell me a fact", "What can you do?"

You can also click the suggestion buttons below the chat interface for quick access to common commands.

## API Endpoints

- `/` - Main chat interface
- `/api/message` - Send messages to the chatbot
- `/api/history` - Get chat history
- `/api/reset` - Reset chat history
- `/api/capabilities` - List chatbot capabilities

## Extending the Chatbot

The chatbot uses a rule-based system in `chatbot.py`. You can extend its capabilities by:

1. Adding new pattern matching rules
2. Extending the `analyze_chat_history` function for better context awareness
3. Adding new response types and categories

## Future Enhancements

- Integration with OpenAI for more intelligent responses
- Multi-user support with authentication
- Persistent chat history with database storage