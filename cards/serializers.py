from rest_framework import serializers

from . import models


class CardSerializer(serializers.ModelSerializer):
    """Serializer for the Card model"""

    class Meta:
        model = models.Card
        fields = (
            'id', 'card_type', 'card_number', 'expiry_date'
        )
        read_only_fields = ('id',)
