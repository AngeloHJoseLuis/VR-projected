// 3. Modificar el Frontend para recibir notificaciones
const notificationSocket = new WebSocket('ws://127.0.0.1:8000/ws/notifications/');

notificationSocket.onmessage = function(event) {
    const data = JSON.parse(event.data);
    alert("🔔 Notificación: " + data.message);
};

// Función para enviar notificación cuando se sube un modelo
function sendNotification(message) {
    notificationSocket.send(JSON.stringify({ 'message': message }));
}