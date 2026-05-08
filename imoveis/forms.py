from django import forms
from .models import Imovel


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = '__all__'

        widgets = {
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'finalidade': forms.Select(attrs={'class': 'form-select'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }


class RetiradaForm(forms.Form):
    nome_cliente = forms.CharField(
        label='Nome do cliente',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do cliente'
        })
    )

    telefone_cliente = forms.CharField(
        label='Telefone do cliente',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o telefone do cliente'
        })
    )
