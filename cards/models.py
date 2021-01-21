from django.db import models
from django.utils import timezone

from dateutil.relativedelta import relativedelta


class CardType(models.Model):
    """Model for storing the types of cards"""
    name = models.CharField(max_length=250)
    service_rate = models.TextField(
        help_text="Python operation, can use Django timezone library"
    )

    class Meta:
        verbose_name = "Card Type"
        verbose_name_plural = "Card Types"

    def __str__(self):
        return self.name


class Card(models.Model):
    """Model for storing cards"""
    card_type = models.ForeignKey(CardType, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    cardholder = models.ForeignKey(
        'persons.Person', on_delete=models.CASCADE, related_name='cards'
    )
    expiry_date = models.DateField(
        default=timezone.now()+relativedelta(years=4)
    )

    def __str__(self):
        return self.card_number
