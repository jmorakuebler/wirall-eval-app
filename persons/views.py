from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins

from .permissions import IsSuperUser
from . import serializers
from . import models


class PersonViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = serializers.PersonSerializer
    permission_classes = (IsAuthenticated, IsSuperUser)
    queryset = models.Person.objects.all()
    operation_limit = 10000
