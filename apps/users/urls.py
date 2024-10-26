from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from apps.users.views import LoginViewSet, UserAPI

router = DefaultRouter()
router.register(r'register', UserAPI, basename='api-register')
router.register(r'login', LoginViewSet, basename='api-login')

urlpatterns = [
    path('register-jwt/', TokenObtainPairView.as_view(), name='api-register-jwt'),
    path('refresh-access/', TokenRefreshView.as_view(), name='api-refresh-access'),
]

urlpatterns += router.urls
