from django.shortcuts import render, redirect
from .models import Imovel
from .forms import ImovelForm


def imovel_list(request):
    imoveis = Imovel.objects.all().order_by('codigo')

    return render(request, 'imoveis/list.html', {
        'imoveis': imoveis
    })


def imovel_create(request):
    form = ImovelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('imovel_list')

    return render(request, 'imoveis/form.html', {
        'form': form
    })
