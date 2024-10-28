import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("WebSocket connection initiated.")
        try:
            await self.channel_layer.group_add("notifications", self.channel_name)
            await self.accept()
            logger.info("WebSocket connection accepted.")
        except Exception as e:
            logger.error(f"Error during WebSocket connection: {str(e)}")
            await self.close()

    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected with close code: {close_code}")
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def send_notification(self, event):
        try:
            message = event['message']
            logger.info(f"Отправка уведомления: {message}")
            await self.send(text_data=json.dumps({
                'type': 'notification',
                'message': message
            }))
            logger.info("Уведомление отправлено через WebSocket.")
        except Exception as e:
            logger.error(f"Ошибка при отправке уведомления: {str(e)}")

    async def delete_notification(self, event):
        try:
            notification_id = event['notification_id']
            logger.info(f"Удаление уведомления с ID: {notification_id}")
            await self.send(text_data=json.dumps({
                'type': 'delete',
                'notification_id': notification_id,
            }))
            logger.info("Сообщение об удалении отправлено через WebSocket.")
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения об удалении: {str(e)}")
