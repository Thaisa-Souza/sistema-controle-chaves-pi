from django import forms
from .models import Imovel


class ImovelForm(forms.ModelForm):
    class Meta:
        model = Imovel
        fields = [
            'codigo',
            'endereco',
            'bairro',
            'tipo',
            'status',
            'foto'
        ]

        widgets = {
            'codigo': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Código do imóvel'
            }),
            'endereco': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Endereço'
            }),
            'bairro': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Bairro'
            }),
            'tipo': forms.Select(attrs={
                'class': 'form-select'
            }),
            'status': forms.Select(attrs={
                'class': 'form-select'
            }),
            'foto': forms.ClearableFileInput(attrs={
                'class': 'form-control'
            }),
        }

        labels = {
            'codigo': 'Código',
            'endereco': 'Endereço',
            'bairro': 'Bairro',
            'tipo': 'Tipo de imóvel',
            'status': 'Status',
            'foto': 'Foto',
        }


class RetiradaForm(forms.Form):
    nome_cliente = forms.CharField(
        label='Nome do cliente',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o nome do cliente'
        })
    )

    telefone_cliente = forms.CharField(
        label='Telefone',
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Digite o telefone do cliente'
        })
    )