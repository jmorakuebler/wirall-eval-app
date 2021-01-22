from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from .serializers import DRFAuthTokenSerializer


class CreateDRFTokenView(ObtainAuthToken):
    """Create new token for user"""
    serializer_class = DRFAuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
