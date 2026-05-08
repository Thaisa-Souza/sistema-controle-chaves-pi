from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db import models
from django.db.models import Count

from .models import Imovel, Chave, Movimentacao
from .forms import ImovelForm, RetiradaForm


@login_required
def imovel_list(request):
    query = request.GET.get('q', '')
    status = request.GET.get('status', '')

    imoveis = Imovel.objects.annotate(
        total_visitas=Count(
            'chave__movimentacao',
            filter=models.Q(chave__movimentacao__acao='retirada')
        )
    )

    if query:
        imoveis = imoveis.filter(
            codigo__icontains=query
        ) | imoveis.filter(
            endereco__icontains=query
        ) | imoveis.filter(
            bairro__icontains=query
        )

    if status:
        imoveis = imoveis.filter(status=status)

    imoveis = imoveis.order_by('codigo')

    paginator = Paginator(imoveis, 6)
    page = request.GET.get('page')
    imoveis = paginator.get_page(page)

    return render(request, 'imoveis/list.html', {
        'imoveis': imoveis,
        'query': query,
        'status_atual': status
    })


@login_required
def imovel_create(request):
    form = ImovelForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Imóvel adicionado com sucesso!')
        return redirect('imovel_list')

    return render(request, 'imoveis/form.html', {
        'form': form,
        'title': 'Adicionar imóvel'
    })


@login_required
def imovel_update(request, pk):
    imovel = get_object_or_404(Imovel, pk=pk)

    form = ImovelForm(
        request.POST or None,
        request.FILES or None,
        instance=imovel
    )

    if form.is_valid():
        form.save()
        messages.success(request, 'Imóvel editado com sucesso!')
        return redirect('imovel_list')

    return render(request, 'imoveis/form.html', {
        'form': form,
        'title': 'Editar imóvel'
    })


@login_required
def imovel_delete(request, pk):
    if not request.user.is_superuser and not request.user.groups.filter(name='Gerentes').exists():
        return redirect('imovel_list')

    imovel = get_object_or_404(Imovel, pk=pk)

    if request.method == 'POST':
        imovel.delete()
        messages.success(request, 'Imóvel excluído com sucesso!')
        return redirect('imovel_list')

    return render(request, 'imoveis/confirm_delete.html', {
        'imovel': imovel
    })


@login_required
def chave_list(request):
    status = request.GET.get('status', '')

    chaves = Chave.objects.select_related('imovel').all().order_by('imovel__codigo')

    if status:
        chaves = chaves.filter(status=status)

    paginator = Paginator(chaves, 10)
    page = request.GET.get('page')
    chaves = paginator.get_page(page)

    return render(request, 'imoveis/chave_list.html', {
        'chaves': chaves,
        'status_atual': status
    })


@login_required
def retirar_chave(request, pk):
    chave = get_object_or_404(Chave, pk=pk)

    if chave.status != 'disponivel':
        return redirect('chave_list')

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

            messages.success(request, 'Chave retirada com sucesso!')
            return redirect('chave_list')

    else:
        form = RetiradaForm()

    return render(request, 'imoveis/retirar_chave.html', {
        'form': form,
        'chave': chave
    })


@login_required
def devolver_chave(request, pk):
    chave = get_object_or_404(Chave, pk=pk)

    if chave.status == 'disponivel':
        return redirect('chave_list')

    ultima_retirada = Movimentacao.objects.filter(
        chave=chave,
        acao='retirada'
    ).order_by('-data').first()

    chave.status = 'disponivel'
    chave.save()

    Movimentacao.objects.create(
        chave=chave,
        acao='devolucao',
        usuario=request.user,
        nome_cliente=ultima_retirada.nome_cliente if ultima_retirada else '',
        telefone_cliente=ultima_retirada.telefone_cliente if ultima_retirada else ''
    )

    messages.success(request, 'Chave devolvida com sucesso!')
    return redirect('chave_list')


@login_required
def historico_list(request):
    query = request.GET.get('q', '')

    movimentacoes = Movimentacao.objects.select_related(
        'chave__imovel',
        'chave__imovel__tipo',
        'usuario'
    ).all()

    if query:
        movimentacoes = movimentacoes.filter(
            models.Q(chave__imovel__codigo__icontains=query) |
            models.Q(chave__imovel__endereco__icontains=query) |
            models.Q(chave__imovel__bairro__icontains=query) |
            models.Q(chave__imovel__tipo__nome__icontains=query) |
            models.Q(chave__imovel__status__icontains=query) |
            models.Q(nome_cliente__icontains=query) |
            models.Q(telefone_cliente__icontains=query) |
            models.Q(usuario__username__icontains=query) |
            models.Q(acao__icontains=query)
        )

    movimentacoes = movimentacoes.order_by('-data')

    paginator = Paginator(movimentacoes, 10)
    page = request.GET.get('page')
    movimentacoes = paginator.get_page(page)

    return render(request, 'imoveis/historico_list.html', {
        'movimentacoes': movimentacoes,
        'query': query
    })


@login_required
def dashboard(request):
    total_imoveis = Imovel.objects.count()
    chaves_disponiveis = Chave.objects.filter(status='disponivel').count()
    chaves_retiradas = Chave.objects.filter(status='retirada').count()
    total_visitas = Movimentacao.objects.filter(acao='retirada').count()

    ultimas_movimentacoes = Movimentacao.objects.select_related(
        'chave__imovel',
        'usuario'
    ).order_by('-data')[:5]

    return render(request, 'imoveis/dashboard.html', {
        'total_imoveis': total_imoveis,
        'chaves_disponiveis': chaves_disponiveis,
        'chaves_retiradas': chaves_retiradas,
        'total_visitas': total_visitas,
        'ultimas_movimentacoes': ultimas_movimentacoes,
    })