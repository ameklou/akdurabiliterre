from django import forms
from .models import Ville, Category

class SearchForm(forms.Form):
    ville=forms.ModelChoiceField(queryset=Ville.objects.all(), widget=forms.Select(attrs={'class':'custom-select mr-sm-2 mb-2 mb-sm-0'}),empty_label='Selectionner une ville')
    category=forms.ModelChoiceField(queryset=Category.objects.all(),empty_label='Selectionner une categorie', widget=forms.Select(attrs={'class':'custom-select mr-sm-2 mb-2 mb-sm-0'}))
