from django import forms
from django.contrib.auth.models import User

from persons.models import Person
from cards.models import CardType


class PersonForm(forms.Form):
    user = forms.ModelChoiceField(queryset=User.objects.all())
    address =  forms.CharField(widget=forms.Textarea)


class CardForm(forms.Form):
    card_type = forms.ModelChoiceField(
        queryset=CardType.objects.all(), empty_label="Select a card type"
    )
    card_number = forms.CharField(max_length=16)
    expiry_date = forms.DateField()
