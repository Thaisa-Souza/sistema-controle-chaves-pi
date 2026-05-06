from django.db import models


class TipoImovel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    codigo = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoImovel, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(
        max_length=50,
        choices=[
            ('disponivel', 'Disponível'),
            ('analise', 'Em análise'),
            ('alugado', 'Alugado'),
            ('inativo', 'Inativo'),
        ],
        default='disponivel'
    )
    foto = models.ImageField(upload_to='imoveis/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.codigo} - {self.endereco}"
