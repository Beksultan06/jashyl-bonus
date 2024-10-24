from rest_framework import serializers
from apps.base.models import Partners

class PartnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Partners
        fields = ['title', 'logo']