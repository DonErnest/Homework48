from django import forms
from django.forms import widgets


class SearchForm(forms.Form):
    search_text = forms.CharField(max_length=100, required=True,
                                  widget=widgets.TextInput(attrs={'placeholder': 'Search', 'type': 'search'}))
