from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.users.views import LoginViewSet, UserAPI

router = DefaultRouter()
router.register(r"register", UserAPI, basename='api-register-email')
router.register(r'login', LoginViewSet, basename='api-login')

urlpatterns = [

]

urlpatterns += router.urls