from django.shortcuts import render, redirect, get_object_or_404
from .models import Conta, Transacao
from django.contrib import messages
from .forms import CadastroForm
from django.contrib.auth.decorators import login_required


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
    conta = get_object_or_404(Conta, usuario=request.user)
    transacoes = conta.transacoes.all().order_by('-data')
    return render(request, 'contas/extrato.html', {'conta': conta, 'transacoes': transacoes})


@login_required
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


@login_required
def sacar(request):
    return render(request, 'contas/operacao.html', {'titulo': 'Realizar Saque'})
