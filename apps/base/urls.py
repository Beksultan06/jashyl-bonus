from django.urls import include, path
from rest_framework.routers import DefaultRouter
from apps.base.views import PartnresAPI

router = DefaultRouter()
router.register(r'partners', PartnresAPI, basename='partner'),

urlpatterns = [
    path('', include(router.urls)),
]