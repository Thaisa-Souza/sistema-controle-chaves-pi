from django.db import models
from django.contrib.auth.models import User


class TipoImovel(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)

    def __str__(self):
        return self.nome


class Imovel(models.Model):
    codigo = models.CharField(max_length=50)
    endereco = models.CharField(max_length=200)
    numero = models.CharField(max_length=6)
    bairro = models.CharField(max_length=100)
    tipo = models.ForeignKey(TipoImovel, on_delete=models.PROTECT)
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
    altered_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.codigo} - {self.endereco}, {self.numero}"

class Chave(models.Model):
    imovel = models.OneToOneField(Imovel, on_delete=models.PROTECT)

    STATUS_CHOICES = [
        ('disponivel', 'Disponível'),
        ('retirada', 'Retirada'),
        ('indisponivel', 'Indisponível'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='disponivel'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    altered_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Chave - {self.imovel.codigo} - {self.imovel.endereco} - {self.imovel.numero}"


class Movimentacao(models.Model):
    chave = models.ForeignKey(Chave, on_delete=models.PROTECT)

    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
    )

    nome_cliente = models.CharField(max_length=100)

    telefone_cliente = models.CharField(max_length=20)

    acao = models.CharField(max_length=20)

    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.acao} - {self.chave.imovel.codigo}"


from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=Imovel)
def controlar_chave_do_imovel(sender, instance, created, **kwargs):
    chave, criada = Chave.objects.get_or_create(
        imovel=instance,
        defaults={'status': 'disponivel'}
    )

    if instance.status == 'alugado':
        chave.status = 'indisponivel'

    elif instance.status == 'inativo':
        chave.status = 'indisponivel'

    elif instance.status == 'disponivel':
        chave.status = 'disponivel'

    chave.save()

