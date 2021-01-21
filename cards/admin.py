from django.contrib import admin

from .models import Card, CardType


admin.site.register(CardType)


@admin.register(Card)
class Card(admin.ModelAdmin):
    list_display = ('card_number', 'card_type', 'cardholder', 'expiry_date')
