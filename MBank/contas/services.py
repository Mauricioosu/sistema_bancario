from django.db import transaction
from django.utils import timezone
from .models import Cliente, Conta, Transacao
from decimal import Decimal


class ContaService:
    @staticmethod
    def criar_cliente(nome, cpf, data_nascimento, endereco, senha):
        if Cliente.objects.filter(cpf=cpf).exists():
            raise ValueError("Já existe um cliente com este CPF.")

        cliente = Cliente.objects.create(
            nome=nome,
            cpf=cpf,
            data_nascimento=data_nascimento,
            endereco=endereco,
            senha=senha
        )
        return cliente

    @staticmethod
    def criar_conta(cliente, numero, limite=500.00, limite_saques=3):
        if Conta.objects.filter(numero=numero).exists():
            raise ValueError("Número de conta já existe.")

        conta = Conta.objects.create(
            numero=numero,
            cliente=cliente,
            limite=limite,
            limite_saques=limite_saques
        )
        return conta

    @staticmethod
    @transaction.atomic
    def depositar(conta, valor):
        valor_decimal = Decimal(str(valor))
        if valor_decimal <= 0:
            raise ValueError("O valor do depósito deve ser positivo.")

        conta.saldo += valor_decimal
        conta.save()

        Transacao.objects.create(conta=conta, tipo='DEPOSITO', valor=valor_decimal)
        return conta.saldo

    @staticmethod
    @transaction.atomic
    def sacar(conta, valor):
        valor_decimal = Decimal(str(valor))

        if valor_decimal <= 0:
            raise ValueError("O valor do saque deve ser positivo.")

        if valor_decimal > conta.saldo:
            raise ValueError("Saldo insuficiente.")

        if valor_decimal > conta.limite:
            raise ValueError("O valor excede o limite de saque da conta.")

        hoje = timezone.now().date()
        saques_hoje = Transacao.objects.filter(
            conta=conta,
            tipo='SAQUE',
            data__date=hoje
        ).count()

        if saques_hoje >= conta.limite_saques:
            raise ValueError("Limite diário de saques excedido.")

        conta.saldo -= valor_decimal
        conta.save()

        Transacao.objects.create(conta=conta, tipo='SAQUE', valor=valor_decimal)
        return conta.saldo
