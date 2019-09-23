from django import forms
from django.forms import widgets

from webapp.models import category_choices


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=100, required=True,
                                  widget=widgets.TextInput(attrs={'placeholder': 'Search', 'type': 'search'}))


class ItemForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Наименование')
    description = forms.CharField(max_length=2000, required=False, label='Описание товара', widget=widgets.Textarea)
    category = forms.ChoiceField(choices=category_choices, required=True, label='Категория')
    amount = forms.IntegerField(min_value=0, label='Остаток')
    price = forms.DecimalField(max_digits=7, decimal_places=2, label='Цена')

