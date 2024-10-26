from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from apps.notification.consumers import NotificationConsumer
from django.core.asgi import get_asgi_application
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/notifications/", NotificationConsumer.as_asgi()),
        ])
    ),
})
