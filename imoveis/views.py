from django.shortcuts import render, redirect
from .models import Imovel
from .forms import ImovelForm
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
