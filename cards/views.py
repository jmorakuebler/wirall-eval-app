from django.utils import timezone

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from . import serializers
from . import models


class CardViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CardSerializer
    permission_classes = (IsAuthenticated,)
    queryset = models.Card.objects.all()
    operation_limit = 10000

    def get_queryset(self):
        qs = self.queryset
        user = self.request.user
        if not user.is_staff and not user.is_superuser:
            qs = qs.filter(cardholder=user.person)
        return qs

    @action(methods=['GET'], detail=True, url_path='do-operation')
    def do_operation(self, request, pk=None):
        card = self.get_object()
        response = {}

        if not card.is_valid:
            msg = f"Card is not valid. Expiration date is {card.expiry_date}"
            raise ValidationError(msg, code="validation")

        operation_value = eval(card.card_type.service_rate)

        if operation_value > self.operation_limit:
            msg = f"Operation failed. Operation value is more than " \
                f"{self.operation_limit}. Value is {operation_value}"
            raise ValidationError(msg, code="validation")
        return Response(
            data={'message': "Operation success."},
            status=status.HTTP_200_OK
        )

    @action(methods=['GET'], detail=True, url_path='check-operation')
    def check_operation(self, request, pk=None):
        card = self.get_object()
        operation_value = eval(card.card_type.service_rate)
        response = {}

        response['is_valid'] = operation_value < self.operation_limit

        return Response(
            data=response,
            status=status.HTTP_200_OK
        )
