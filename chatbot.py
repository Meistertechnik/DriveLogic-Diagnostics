import re
import random
import logging
import datetime
import os

def generate_response(user_input, chat_history):
    """
    Generate a response based on the user input and chat history.
    This is an enhanced rule-based chatbot implementation.
    
    Args:
        user_input (str): The user's message
        chat_history (list): The history of the conversation
    
    Returns:
        str: The chatbot's response
    """
    # Convert to lowercase for easier matching
    user_input_lower = user_input.lower()
    
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
    
    # Check for context in chat history
    context = analyze_chat_history(chat_history)
    
    # Process input and generate response
    if any(greeting in user_input_lower for greeting in greetings):
        return random.choice([
            "Hello there! How can I help you today?",
            "Hi! Nice to chat with you. What can I do for you?",
            f"Hey! How's your day going? It's {datetime.datetime.now().strftime('%A')} today.",
            "Greetings! How may I assist you?"
        ])
    
    elif any(farewell in user_input_lower for farewell in farewells):
        return random.choice([
            "Goodbye! Have a great day!",
            "See you later! Feel free to come back if you need anything.",
            "Bye for now! Take care!",
            "Until next time!"
        ])
    
    elif any(thank in user_input_lower for thank in thanks):
        return random.choice([
            "You're welcome!",
            "Happy to help!",
            "Anytime! Is there anything else you need?",
            "My pleasure. What else can I assist you with?"
        ])
    
    elif any(phrase in user_input_lower for phrase in about_bot):
        return random.choice([
            "I'm a Flask-based chatbot created for demonstration purposes. I can have simple conversations and answer basic questions.",
            "I'm your friendly neighborhood chatbot, built with Python Flask and vanilla JavaScript!",
            "I'm a basic AI assistant, designed to respond to your messages and demonstrate web application capabilities.",
            "Just a humble chatbot trying to be helpful. I was created using Flask for the backend and JavaScript for the frontend!"
        ])
    
    elif any(phrase in user_input_lower for phrase in help_requests):
        return "I can help with several things:\n\n" + \
               "• Respond to greetings and farewells\n" + \
               "• Tell jokes and fun facts\n" + \
               "• Provide the current date and time\n" + \
               "• Answer questions about myself\n" + \
               "• Hold simple conversations\n\n" + \
               "What would you like to know more about?"
    
    elif 'weather' in user_input_lower:
        return "I don't have access to real-time weather data, but I hope it's nice wherever you are! If you're building a production app, you could integrate with a weather API."
    
    elif 'time' in user_input_lower or 'date' in user_input_lower:
        now = datetime.datetime.now()
        return f"The current date and time is {now.strftime('%A, %B %d, %Y at %I:%M %p')}."
    
    elif 'joke' in user_input_lower or 'funny' in user_input_lower:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "Did you hear about the mathematician who's afraid of negative numbers? He'll stop at nothing to avoid them!",
            "Why was the computer cold? It left its Windows open!",
            "What do you call a fake noodle? An impasta!",
            "Why don't programmers like nature? It has too many bugs.",
            "Why did the developer go broke? Because he used up all his cache.",
            "What's a computer's favorite snack? Microchips!",
            "Why was the JavaScript developer sad? Because he didn't Node how to Express himself."
        ]
        return random.choice(jokes)
    
    elif 'fact' in user_input_lower or 'interesting' in user_input_lower:
        facts = [
            "The first computer 'bug' was an actual real-life bug. A moth was trapped in a Harvard Mark II computer in 1947.",
            "The average person spends 6 months of their lifetime waiting at traffic lights.",
            "The word 'robot' comes from the Czech word 'robota', which means forced labor or work.",
            "Python programming language wasn't named after a snake but after the British comedy group Monty Python.",
            "A group of flamingos is called a 'flamboyance'.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly good to eat."
        ]
        return random.choice(facts)
    
    elif 'name' in user_input_lower and context.get('discussing_user'):
        return f"Nice to meet you! How can I help you today?"
    
    elif '?' in user_input:
        if re.search(r'(what|who|where|when|why|how)', user_input_lower):
            return random.choice([
                "That's an interesting question! I wish I had more knowledge to give you a better answer.",
                "Great question! Unfortunately, my knowledge is limited on that topic.",
                "I'm not sure about that, but it would be interesting to learn more!",
                "That's something I don't have enough information about yet."
            ])
        else:
            return "I'm not sure I understand your question. Could you rephrase it?"
    
    else:
        # Default responses for when no pattern matches
        return random.choice([
            "I see. Tell me more about that.",
            "Interesting! What else is on your mind?",
            "I'm not sure I fully understand. Could you elaborate?",
            "That's good to know. How can I help you with that?",
            "I'm still learning. Can you tell me more?"
        ])

def analyze_chat_history(chat_history):
    """
    Analyze the chat history to detect context of the conversation.
    
    Args:
        chat_history (list): The history of the conversation
    
    Returns:
        dict: Context information
    """
    context = {
        'discussing_user': False,
        'discussing_tech': False,
        'greeting_exchanged': False
    }
    
    # Only analyze recent messages (last 5)
    recent_messages = chat_history[-5:] if len(chat_history) > 5 else chat_history
    
    for message in recent_messages:
        if message.get('sender') == 'user':
            user_message = message.get('message', '').lower()
            
            # Check for name sharing
            name_patterns = ['my name is', 'i am called', 'i\'m called', 'call me']
            if any(pattern in user_message for pattern in name_patterns):
                context['discussing_user'] = True
            
            # Check for tech discussions
            tech_terms = ['programming', 'code', 'software', 'developer', 'javascript', 'python', 'flask']
            if any(term in user_message for term in tech_terms):
                context['discussing_tech'] = True
            
            # Check for greetings
            greetings = ['hello', 'hi', 'hey', 'greetings']
            if any(greeting in user_message for greeting in greetings):
                context['greeting_exchanged'] = True
    
    return context
