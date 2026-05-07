from django.shortcuts import render, redirect
from .models import Imovel, Chave, Movimentacao
from .forms import ImovelForm, ChaveForm, RetiradaForm
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

def retirar_chave(request, pk):
    chave = get_object_or_404(Chave, pk=pk)

    if request.method == 'POST':
        form = RetiradaForm(request.POST)

        if form.is_valid():

            chave.status = 'retirada'
            chave.save()

            Movimentacao.objects.create(
                chave=chave,
                acao='retirada',
                usuario=request.user,
                nome_cliente=form.cleaned_data['nome_cliente'],
                telefone_cliente=form.cleaned_data['telefone_cliente']
            )

            return redirect('chave_list')

    else:
        form = RetiradaForm()

    return render(request, 'imoveis/retirar_chave.html', {
        'form': form,
        'chave': chave
    })

def devolver_chave(request, pk):
    chave = get_object_or_404(Chave, pk=pk)

    chave.status = 'disponivel'
    chave.save()

    Movimentacao.objects.create(
        chave=chave,
        acao='devolucao',
        usuario=request.user
    )

    return redirect('chave_list')

def historico_list(request):
    movimentacoes = Movimentacao.objects.select_related(
        'chave__imovel',
        'usuario'
    ).all().order_by('-data')

    return render(request, 'imoveis/historico_list.html', {
        'movimentacoes': movimentacoes
    })
