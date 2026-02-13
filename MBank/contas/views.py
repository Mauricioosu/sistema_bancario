from django.shortcuts import render, redirect
from .models import Conta, Transacao
from django.contrib import messages
from .forms import CadastroForm
from django.contrib.auth.decorators import login_required
from decimal import Decimal


def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'usuario e conta criados com Sucesso!')
            return redirect('login')
    else:
        form = CadastroForm()
    return render(request, 'contas/cadastrar.html', {'form': form})


@login_required
def index(request):
    conta = Conta.objects.filter(usuario=request.user).first()
    return render(request, 'contas/index.html', {'conta': conta})


@login_required
def extrato(request):
    try:
        conta = Conta.objects.get(usuario=request.user)
        transacoes = Transacao.objects.filter(conta=conta).order_by('-data')
    except Conta.DoesNotExist:
        return render(request, 'contas/extrato.html', {
            'error': 'Você ainda não possui uma conta ativa.',
            'saldo': 0
        })

    return render(request, 'contas/extrato.html', {
        'transacoes': transacoes,
        'saldo': conta.saldo
    })


@login_required
def depositar(request):
    conta = Conta.objects.first()

    if request.method == "POST":
        valor = float(request.POST.get('valor'))

        if valor > 0:
            conta.saldo += valor
            conta.save()

            Transacao.objects.create(
                conta=conta,
                tipe='D',
                valor=valor
            )
            messages.success(request, f'Deposito de R${valor:.2f} realizado com sucesso!')
            return redirect('extrato')
    return render(request, 'contas/operacao.html', {'titulo': 'realizar deposito'})


@login_required
def sacar(request):
    if request.method == "POST":
        valor = Decimal(request.POST.get('valor'))
        conta = Conta.objects.get(usuario=request.user)

        if 0 < valor <= conta.saldo:
            conta.saldo -= valor
            conta.save()

            # Regista no extrato
            Transacao.objects.create(conta=conta, tipo='S', valor=valor)

            messages.success(request, f"Saque de R$ {valor} realizado!")
            return redirect('index')
        else:
            messages.error(request, "Saldo insuficiente ou valor inválido.")

    return render(request, 'contas/saque.html')
