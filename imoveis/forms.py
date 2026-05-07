from django import forms
from .models import Imovel, Chave


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'


class ChaveForm(forms.ModelForm):
    class Meta:
        model = Chave
        fields = '__all__'
