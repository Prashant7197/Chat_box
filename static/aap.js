// Connect to the WebSocket server using the API endpoint
const socket = new WebSocket('ws://127.0.0.1:8000/api/messages/');

const messageInput = document.getElementById('message-input');
const sendButton = document.getElementById('send-button');
const chatMessages = document.getElementById('chat-messages');

// Function to add a message to the chat container
function addMessage(message, sender) {
    const messageElement = document.createElement('div');
    messageElement.className = sender === 'You' ? 'message sent' : 'message received';
    messageElement.innerText = `${sender}: ${message}`;
    chatMessages.appendChild(messageElement);
    chatMessages.scrollTop = chatMessages.scrollHeight; // Scroll to the latest message
}

// Handle messages received from the server
socket.addEventListener('message', (event) => {
    const data = JSON.parse(event.data);
    addMessage(data.message, 'Friend');
});

// Send a message when the Send button is clicked
sendButton.addEventListener('click', () => {
    const message = messageInput.value;
    if (message) {
        addMessage(message, 'You');
        socket.send(JSON.stringify({ message }));
        messageInput.value = '';
    }
});
