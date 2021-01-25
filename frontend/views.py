from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.base import TemplateView

from persons.models import Person
from cards.models import Card
from . import forms

class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "frontend/main.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_superuser:
            context['card_list'] = Card.objects.all()
        else:
            context['card_list'] = Card.objects.filter(
                cardholder=self.request.user.person
            )
        context['form'] = forms.CardForm()
        return context


class PersonView(UserPassesTestMixin, TemplateView):
    template_name = "frontend/persons.html"

    def test_func(self):
        return self.request.user.is_superuser

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['person_list'] = Person.objects.all()
        context['form'] = forms.PersonForm()
        return context
