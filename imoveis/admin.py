from django.contrib import admin
from .models import Imovel, TipoImovel, Chave, Movimentacao

admin.site.register(Imovel)
admin.site.register(TipoImovel)
admin.site.register(Chave)
admin.site.register(Movimentacao)
