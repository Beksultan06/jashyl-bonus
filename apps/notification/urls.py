from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationAdminViewSet

from apps.notification.routing import websocket_urlpatterns

router = DefaultRouter()
router.register(r'admin-notifications', NotificationAdminViewSet, basename='admin-notifications')

urlpatterns = [
    path('', include(router.urls)),
    path("", include(websocket_urlpatterns))
]
