from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from apps.base.models import Partners
from apps.base.serializers import PartnersSerializers
# Create your views here.

class PartnresAPI(GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,):
    queryset = Partners.objects.all()
    serializer_class = PartnersSerializers
    permission_classes = [IsAuthenticated]