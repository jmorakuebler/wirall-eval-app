from django.db import models
from django.utils import timezone

from dateutil.relativedelta import relativedelta


def default_expiry_date():
    """Set default date to current date plus 4 years"""
    return timezone.now().date() + relativedelta(years=4)


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
    expiry_date = models.DateField(default=default_expiry_date)

    def __str__(self):
        return self.card_number

    @property
    def is_valid(self):
        """Check if card is not expired"""
        return self.expiry_date > timezone.now().date()
