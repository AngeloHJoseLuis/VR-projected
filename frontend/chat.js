const socket = new WebSocket('ws://127.0.0.1:8000/ws/chat/');

socket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    const chatBox = document.getElementById("chat-box");
    chatBox.innerHTML += `<p><strong>${data.user}:</strong> ${data.message}</p>`;
};

function sendMessage() {
    const user = document.getElementById("username").value;
    const message = document.getElementById("message").value;
    socket.send(JSON.stringify({ 'user': user, 'message': message }));
}