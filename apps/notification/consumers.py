# import json
# import logging
# from channels.generic.websocket import AsyncWebsocketConsumer

# logger = logging.getLogger(__name__)

# class NotificationConsumer(AsyncWebsocketConsumer):
#     async def connect(self):
#         logger.info(f"WebSocket connected")
#         # Добавляем подключённого клиента в общую группу уведомлений
#         await self.channel_layer.group_add(
#             "notifications",  # Общая группа
#             self.channel_name
#         )
#         await self.accept()

#     async def disconnect(self, close_code):
#         logger.info(f"WebSocket disconnected")
#         # Убираем подключённого клиента из общей группы
#         await self.channel_layer.group_discard(
#             "notifications",
#             self.channel_name
#         )

#     async def send_notification(self, event):
#         message = event['message']
#         logger.info(f"Отправляем уведомление через WebSocket: {message}")
#         await self.send(text_data=json.dumps({
#             'message': message
#         }))

import json
import logging
from channels.generic.websocket import AsyncWebsocketConsumer

logger = logging.getLogger(__name__)

class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.info("WebSocket connection initiated.")
        await self.accept()
        logger.info("WebSocket connection accepted.")

    async def disconnect(self, close_code):
        logger.info(f"WebSocket disconnected with close code: {close_code}")

    async def send_notification(self, event):
        message = event['message']
        logger.info(f"Sending notification: {message}")
        await self.send(text_data=json.dumps({
            'message': message
        }))
        logger.info("Notification sent to WebSocket.")
