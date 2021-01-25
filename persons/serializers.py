from rest_framework import serializers

from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    """Serializer for the Person model"""

    class Meta:
        model = Person
        fields = ('id', 'user', 'address')
        read_only_fields = ('id',)
