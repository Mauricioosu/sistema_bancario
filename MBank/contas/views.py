from django.shortcuts import render, redirect
from .models import Conta, Transacao
from django.contrib import messages
from .forms import CadastroForm


def extrato(request):
    contexto = {
        'transacoes': [],
        'conta': {'saldo': 0.00}
    }
    return render(request, 'contas/extrato.html', contexto)


def index(request):
    return render(request, 'contas/index.html')


def cadastrar(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'usuario e conta criados com Sucesso!')
            return redirect('login')


def depositar(request):
    conta = Conta.obejcts.first()

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

def sacar(request):
    return render(request, 'contas/operacao.html', {'titulo': 'Realizar Saque'})
