// const socket = new WebSocket('ws://127.0.0.1:8000/ws/chat/');

// socket.onmessage = function(event) {
//     const data = JSON.parse(event.data);
//     const chatBox = document.getElementById("chat-box");
//     chatBox.innerHTML += `<p><strong>${data.user}:</strong> ${data.message}</p>`;
// };

// function sendMessage() {
//     const user = document.getElementById("username").value;
//     const message = document.getElementById("message").value;
//     socket.send(JSON.stringify({ 'user': user, 'message': message }));
// }

let socket;

function connectWebSocket() {
    socket = new WebSocket("ws://127.0.0.1:8000/ws/chat/");

    socket.onopen = function () {
        console.log("🔗 Conectado al WebSocket del chat.");
    };

    socket.onmessage = function (event) {
        try {
            const data = JSON.parse(event.data);
            const chatBox = document.getElementById("chat-box");
            if (!chatBox) {
                console.error("❌ No se encontró el chat-box en el DOM.");
                return;
            }
            chatBox.innerHTML += `<p><strong>${data.user}:</strong> ${data.message}</p>`;
        } catch (error) {
            console.error("❌ Error al procesar el mensaje:", error);
        }
    };

    socket.onerror = function (error) {
        console.error("❌ Error en WebSocket:", error);
    };

    socket.onclose = function () {
        console.warn("⚠️ Conexión WebSocket cerrada. Intentando reconectar en 3 segundos...");
        setTimeout(connectWebSocket, 3000);
    };
}

function sendMessage() {
    const user = document.getElementById("username").value.trim();
    const message = document.getElementById("message").value.trim();

    if (!user || !message) {
        alert("⚠️ El nombre y el mensaje no pueden estar vacíos.");
        return;
    }

    if (socket.readyState === WebSocket.OPEN) {
        socket.send(JSON.stringify({ user: user, message: message }));
    } else {
        console.warn("⚠️ No hay conexión con WebSocket. Intentando reconectar...");
        connectWebSocket();
    }
}

// Iniciar la conexión WebSocket al cargar la página
connectWebSocket();
