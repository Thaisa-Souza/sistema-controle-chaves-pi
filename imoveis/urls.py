from django.urls import path
from . import views

urlpatterns = [
    path('', views.imovel_list, name='imovel_list'),
    path('novo/', views.imovel_create, name='imovel_create'),

    path('editar/<int:pk>/', views.imovel_update, name='imovel_update'),

    path('excluir/<int:pk>/', views.imovel_delete, name='imovel_delete'),

    path('chaves/', views.chave_list, name='chave_list'),

    path('chaves/nova/', views.chave_create, name='chave_create'),

    path(
    'chaves/retirar/<int:pk>/',
    views.retirar_chave,
    name='retirar_chave'
),

path(
    'chaves/devolver/<int:pk>/',
    views.devolver_chave,
    name='devolver_chave'
),

]
