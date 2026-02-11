from django.shortcuts import render


def extrato(request):
    contexto = {
        'transacoes': [],
        'conta': {'saldo': 0.00}
    }
    return render(request, 'contas/extrato.html', contexto)

def index(request):
    return render(request, 'contas/index.html')

def depositar(request):
    return render(request, 'contas/operacao.html', {'titulo': 'Realizar Depósito'})

def sacar(request):
    return render(request, 'contas/operacao.html', {'titulo': 'Realizar Saque'})
