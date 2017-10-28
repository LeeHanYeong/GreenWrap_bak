from rest_framework import serializers

from ..models import VinylInfo


class VinylInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = VinylInfo
        fields = (
            'thickness',
            'material',
        )
