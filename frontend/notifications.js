let notificationSocket;

function connectWebSocket() {
    notificationSocket = new WebSocket("ws://127.0.0.1:8000/ws/notifications/");

    notificationSocket.onopen = function () {
        console.log("🔗 Conectado al WebSocket de notificaciones.");
    };

    notificationSocket.onmessage = function (event) {
        try {
            const data = JSON.parse(event.data);
            if (data.message) {
                alert("🔔 Notificación: " + data.message);
            } else {
                console.warn("⚠️ Notificación sin mensaje recibido:", data);
            }
        } catch (error) {
            console.error("❌ Error al procesar la notificación:", error);
        }
    };

    notificationSocket.onerror = function (error) {
        console.error("❌ Error en WebSocket:", error);
    };

    notificationSocket.onclose = function () {
        console.warn("⚠️ Conexión WebSocket cerrada. Intentando reconectar en 3 segundos...");
        setTimeout(connectWebSocket, 3000);
    };
}

// Función para enviar notificaciones al servidor
function sendNotification(message) {
    if (!message.trim()) {
        console.warn("⚠️ No se puede enviar una notificación vacía.");
        return;
    }

    if (notificationSocket.readyState === WebSocket.OPEN) {
        notificationSocket.send(JSON.stringify({ message: message }));
    } else {
        console.warn("⚠️ WebSocket no conectado. Intentando reconectar...");
        connectWebSocket();
    }
}

// Iniciar conexión WebSocket al cargar la página
connectWebSocket();

// 3. Modificar el Frontend para recibir notificaciones
// const notificationSocket = new WebSocket('ws://127.0.0.1:8000/ws/notifications/');

// notificationSocket.onmessage = function(event) {
//     const data = JSON.parse(event.data);
//     alert("🔔 Notificación: " + data.message);
// };

// // Función para enviar notificación cuando se sube un modelo
// function sendNotification(message) {
//     notificationSocket.send(JSON.stringify({ 'message': message }));
// }