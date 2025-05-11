document.addEventListener('DOMContentLoaded', function() {
    // DOM Elements
    const chatContainer = document.getElementById('chat-container');
    const messageForm = document.getElementById('message-form');
    const userInput = document.getElementById('user-input');
    const sendButton = document.getElementById('send-button');
    const typingIndicator = document.getElementById('typing-indicator');
    const resetButton = document.getElementById('reset-button');
    const emptyState = document.getElementById('empty-state');

    // Fetch and display chat history on page load
    loadChatHistory();

    // Event listeners
    messageForm.addEventListener('submit', sendMessage);
    resetButton.addEventListener('click', resetChat);
    userInput.addEventListener('input', toggleSendButton);

    // Enable/disable send button based on input
    function toggleSendButton() {
        if (userInput.value.trim() === '') {
            sendButton.disabled = true;
        } else {
            sendButton.disabled = false;
        }
    }

    // Initialize button state
    toggleSendButton();

    // Send message function
    async function sendMessage(e) {
        e.preventDefault();
        
        const message = userInput.value.trim();
        if (!message) return; // Don't send empty messages
        
        // Clear input field and disable send button
        userInput.value = '';
        sendButton.disabled = true;
        
        // Append user message to chat
        appendMessage('user', message);
        
        // Show typing indicator
        showTypingIndicator();
        
        try {
            // Send message to server
            const response = await fetch('/chat', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ message })
            });
            
            if (!response.ok) {
                throw new Error('Failed to get response');
            }
            
            const data = await response.json();
            
            // Hide typing indicator
            hideTypingIndicator();
            
            // Add bot response to chat
            appendMessage('bot', data.reply);
            
            // Scroll to bottom of chat
            scrollToBottom();
            
        } catch (error) {
            console.error('Error:', error);
            hideTypingIndicator();
            
            // Show error message in chat
            appendMessage('bot', 'Sorry, there was an error processing your message. Please try again.');
            scrollToBottom();
        }
    }

    // Load chat history
    async function loadChatHistory() {
        try {
            const response = await fetch('/api/history');
            const data = await response.json();
            
            // If history exists, hide empty state and display messages
            if (data.history && data.history.length > 0) {
                emptyState.style.display = 'none';
                
                // Add all messages to chat
                data.history.forEach(item => {
                    appendMessage(item.sender, item.message);
                });
                
                scrollToBottom();
            } else {
                // Show empty state if no history
                emptyState.style.display = 'flex';
            }
            
        } catch (error) {
            console.error('Error loading chat history:', error);
            // If there's an error, just show the empty state
            emptyState.style.display = 'flex';
        }
    }

    // Reset chat history
    async function resetChat() {
        try {
            const response = await fetch('/api/reset', {
                method: 'POST'
            });
            
            if (!response.ok) {
                throw new Error('Failed to reset chat');
            }
            
            // Clear the chat container
            chatContainer.innerHTML = '';
            
            // Show empty state
            emptyState.style.display = 'flex';
            
        } catch (error) {
            console.error('Error resetting chat:', error);
            alert('Failed to reset chat. Please try again.');
        }
    }

    // Append a message to the chat
    function appendMessage(sender, message) {
        // Hide empty state if visible
        if (emptyState.style.display !== 'none') {
            emptyState.style.display = 'none';
        }
        
        // Create message element
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('message', sender === 'user' ? 'user-message' : 'bot-message');
        messageDiv.textContent = message;
        
        chatContainer.appendChild(messageDiv);
        scrollToBottom();
    }

    // Show typing indicator
    function showTypingIndicator() {
        typingIndicator.style.display = 'block';
        scrollToBottom();
    }

    // Hide typing indicator
    function hideTypingIndicator() {
        typingIndicator.style.display = 'none';
    }

    // Scroll to the bottom of the chat container
    function scrollToBottom() {
        chatContainer.scrollTop = chatContainer.scrollHeight;
    }
    
    // Make suggestMessage available globally
    window.suggestMessage = function(text) {
        userInput.value = text;
        sendButton.disabled = false;
        userInput.focus();
    };
});
