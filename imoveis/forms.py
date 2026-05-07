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

class RetiradaForm(forms.Form):
    nome_cliente = forms.CharField(max_length=100)

    telefone_cliente = forms.CharField(max_length=20)
