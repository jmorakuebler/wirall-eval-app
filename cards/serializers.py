from rest_framework import serializers

from . import models


class CardSerializer(serializers.ModelSerializer):
    """Serializer for the Card model"""
    cardholder = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = models.Card
        fields = (
            'id', 'card_type', 'card_number', 'cardholder', 'expiry_date'
        )
