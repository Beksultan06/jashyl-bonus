from django.contrib import admin
from .models import Notification
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import logging

logger = logging.getLogger(__name__)

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'created_at')
    list_filter = ('user', 'message', 'created_at')
    search_fields = ('user', 'message', 'created_at')

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)

        channel_layer = get_channel_layer()
        if channel_layer is None:
            logger.error("Канал уведомлений не настроен.")
            return

        try:
            logger.info("Отправка уведомления через канал.")
            async_to_sync(channel_layer.group_send)(
                "notifications",
                {
                    "type": "send_notification",
                    "message": obj.message
                }
            )
            logger.info("Уведомление отправлено успешно.")
        except Exception as e:
            logger.error(f"Ошибка при отправке уведомления: {str(e)}")

    def delete_model(self, request, obj):
        notification_id = obj.id
        super().delete_model(request, obj)

        channel_layer = get_channel_layer()
        if channel_layer is None:
            logger.error("Канал уведомлений не настроен.")
            return

        try:
            logger.info(f"Отправка сообщения об удалении уведомления с ID {notification_id} через канал.")
            async_to_sync(channel_layer.group_send)(
                "notifications",
                {
                    "type": "delete_notification",
                    "notification_id": notification_id,
                }
            )
            logger.info(f"Сообщение об удалении уведомления с ID {notification_id} отправлено успешно.")
        except Exception as e:
            logger.error(f"Ошибка при отправке сообщения об удалении: {str(e)}")




