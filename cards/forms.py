
from django.forms import ModelForm

from cards.models import Card, Set


class AddCardForm(ModelForm):
    class Meta:
        model = Card
        fields = ['question', 'answer', 'card_set']


class CreateSetForm(ModelForm):
    class Meta:
        model = Set
        fields = ['name', 'description',
                  'term_language', 'definition_language']
