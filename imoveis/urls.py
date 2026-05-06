from django.urls import path
from . import views

urlpatterns = [
    path('', views.imovel_list, name='imovel_list'),
    path('novo/', views.imovel_create, name='imovel_create'),
]
