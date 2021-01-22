from django.contrib.auth import authenticate

from rest_framework import serializers


class DRFAuthTokenSerializer(serializers.Serializer):
    """Serialize for authentication of DRF users"""
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        username = attrs.get('username')
        password = attrs.get('password')

        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        if not user:
            msg = "Could not authenticate with given credentials"
            raise serializers.ValidationError(msg, code='authentication')
        attrs['user'] = user
        return attrs