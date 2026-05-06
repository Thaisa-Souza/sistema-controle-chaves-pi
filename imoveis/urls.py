from django.urls import path
from . import views

urlpatterns = [
    path('', views.imovel_list, name='imovel_list'),
    path('novo/', views.imovel_create, name='imovel_create'),

    path('editar/<int:pk>/', views.imovel_update, name='imovel_update'),

    path('excluir/<int:pk>/', views.imovel_delete, name='imovel_delete'),
]
