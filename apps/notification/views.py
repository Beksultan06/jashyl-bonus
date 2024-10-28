from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from apps.notification.serializers import NotificationSerializer
from .models import Notification
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

class NotificationAdminViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        logger.info("Начало создания уведомления.")
        notification = serializer.save()
        logger.info(f"Уведомление создано: {notification.message}")

        channel_layer = get_channel_layer()
        if channel_layer is None:
            logger.error("Канал уведомлений не настроен.")
            return Response({
                'status': 'error',
                'message': 'Канал уведомлений не настроен.',
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        try:
            logger.info("Отправка уведомления через канал.")
            async_to_sync(channel_layer.group_send)(
                "notifications",
                {
                    "type": "send_notification",
                    "message": notification.message
                }
            )
            logger.info("Уведомление отправлено успешно.")
        except Exception as e:
            logger.error(f"Ошибка при отправке уведомления: {str(e)}")
            return Response({
                'status': 'error',
                'message': f'Ошибка при отправке уведомления: {str(e)}'
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response({
            'status': 'success',
            'message': notification.message
        }, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def notifications_page(request):
    logger.info("Запрос страницы уведомлений.")
    return render(request, 'notifications.html')