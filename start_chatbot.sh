#!/bin/bash

# Start Flask application in production mode with gunicorn
echo "Starting Flask Chatbot Application..."
gunicorn --bind 0.0.0.0:5000 main:app