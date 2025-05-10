import re
import random
import logging

def generate_response(user_input, chat_history):
    """
    Generate a response based on the user input and chat history.
    This is a simple rule-based chatbot implementation.
    
    Args:
        user_input (str): The user's message
        chat_history (list): The history of the conversation
    
    Returns:
        str: The chatbot's response
    """
    # Convert to lowercase for easier matching
    user_input = user_input.lower()
    
    # Greeting patterns
    greetings = ['hello', 'hi', 'hey', 'howdy', 'greetings', 'sup', 'what\'s up']
    
    # Farewell patterns
    farewells = ['bye', 'goodbye', 'see you', 'exit', 'quit', 'later']
    
    # Thank you patterns
    thanks = ['thank', 'thanks', 'appreciate', 'grateful']
    
    # Questions about the bot
    about_bot = ['who are you', 'what are you', 'your name', 'who created you', 'what can you do']
    
    # Help requests
    help_requests = ['help', 'assist', 'support', 'guide', 'how to']
    
    # Process input and generate response
    if any(greeting in user_input for greeting in greetings):
        return random.choice([
            "Hello there! How can I help you today?",
            "Hi! Nice to chat with you. What can I do for you?",
            "Hey! How's your day going?",
            "Greetings! How may I assist you?"
        ])
    
    elif any(farewell in user_input for farewell in farewells):
        return random.choice([
            "Goodbye! Have a great day!",
            "See you later! Feel free to come back if you need anything.",
            "Bye for now! Take care!",
            "Until next time!"
        ])
    
    elif any(thank in user_input for thank in thanks):
        return random.choice([
            "You're welcome!",
            "Happy to help!",
            "Anytime! Is there anything else you need?",
            "My pleasure. What else can I assist you with?"
        ])
    
    elif any(phrase in user_input for phrase in about_bot):
        return random.choice([
            "I'm a simple chatbot created for demonstration purposes.",
            "I'm your friendly neighborhood chatbot, here to chat and help!",
            "I'm a basic AI assistant, designed to respond to your messages.",
            "Just a humble chatbot trying to be helpful. What can I do for you?"
        ])
    
    elif any(phrase in user_input for phrase in help_requests):
        return "I can respond to greetings, answer questions about myself, and have simple conversations. What would you like to talk about?"
    
    elif 'weather' in user_input:
        return "I don't have access to real-time weather data, but I hope it's nice wherever you are!"
    
    elif 'time' in user_input:
        return "I don't have access to the current time, but your device should show it somewhere on screen."
    
    elif 'joke' in user_input or 'funny' in user_input:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Why was the computer cold? It left its Windows open!",
            "What do you call a fake noodle? An impasta!"
        ]
        return random.choice(jokes)
    
    elif '?' in user_input:
        return random.choice([
            "That's an interesting question! I wish I had more knowledge to give you a better answer.",
            "Great question! Unfortunately, my knowledge is limited on that topic.",
            "I'm not sure about that, but it would be interesting to learn more!",
            "That's something I don't have enough information about yet."
        ])
    
    else:
        # Default responses for when no pattern matches
        return random.choice([
            "I see. Tell me more about that.",
            "Interesting! What else is on your mind?",
            "I'm not sure I fully understand. Could you elaborate?",
            "That's good to know. How can I help you with that?",
            "I'm still learning. Can you tell me more?"
        ])
