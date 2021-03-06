from django.utils import timezone

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.serializers import ValidationError
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from . import serializers
from . import models


class CardViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = serializers.CardSerializer
    permission_classes = (IsAuthenticated,)
    queryset = models.Card.objects.all()
    operation_limit = 1000

    def get_queryset(self):
        qs = self.queryset
        user = self.request.user
        if not user.is_superuser:
            qs = qs.filter(cardholder=user.person)
        return qs

    def perform_create(self, serializer):
        card = serializer.save(cardholder=self.request.user.person)

    @action(methods=['GET'], detail=True, url_path='make-operation')
    def make_operation(self, request, pk=None):
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

    @action(methods=['GET'], detail=False, url_path='check-card-number')
    def check_card_number(self, request):
        card_number = request.query_params.get('card_number')
        data = {'is_available': None}
        if card_number:
            is_available = models.Card.objects.filter(
                card_number=card_number
            ).exists()
            data['is_available'] = not is_available
        return Response(
            data=data,
            status=status.HTTP_200_OK
        )
