from django.shortcuts import render, redirect
from .models import Imovel, Chave
from .forms import ImovelForm, ChaveForm
from django.shortcuts import get_object_or_404


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


def imovel_update(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)

    form = ImovelForm(
        request.POST or None,
        request.FILES or None,
        instance=imovel
    )

    if form.is_valid():
        form.save()
        return redirect('imovel_list')

    return render(request, 'imoveis/form.html', {
        'form': form
    })


def imovel_delete(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)

    if request.method == 'POST':
        imovel.delete()
        return redirect('imovel_list')

    return render(request, 'imoveis/confirm_delete.html', {
        'imovel': imovel
    })

def chave_list(request):
    chaves = Chave.objects.select_related('imovel').all()

    return render(request, 'imoveis/chave_list.html', {
        'chaves': chaves
    })


def chave_create(request):
    form = ChaveForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('chave_list')

    return render(request, 'imoveis/chave_form.html', {
        'form': form
    })
