from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NotificationAdminViewSet

router = DefaultRouter()
router.register(r'admin-notifications', NotificationAdminViewSet, basename='admin-notifications')

urlpatterns = [
    path('', include(router.urls)),
    
]
