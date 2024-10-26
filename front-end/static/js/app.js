document.addEventListener("DOMContentLoaded", function() {
    // Подключение к WebSocket серверу
    const wsUrl = `ws://${window.location.host}/ws/notifications/`;
    const notificationSocket = new WebSocket(wsUrl);

    // Когда WebSocket соединение открыто
    notificationSocket.onopen = function(e) {
        console.log("WebSocket подключен.");
    };

    // Когда сервер отправляет сообщение
    notificationSocket.onmessage = function(e) {
        const data = JSON.parse(e.data);
        const message = data.message;

        // Добавляем уведомление в список
        const notificationsList = document.getElementById("notifications");
        const newNotification = document.createElement("li");
        newNotification.textContent = message;
        notificationsList.appendChild(newNotification);
    };

    // Когда WebSocket соединение закрыто
    notificationSocket.onclose = function(e) {
        console.log('WebSocket закрыт.');
    };

    // Обработка ошибок WebSocket
    notificationSocket.onerror = function(e) {
        console.error('Ошибка WebSocket:', e);
    };
});
