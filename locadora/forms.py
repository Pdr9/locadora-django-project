from django import forms
from locadora.models import Locacao, Filme

class LocacaoForm(forms.ModelForm):
    class Meta:
        model = Locacao
        fields = '__all__'

class FilmeForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'
