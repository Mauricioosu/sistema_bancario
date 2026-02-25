from django.db import models
from django.utils import timezone


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    data_nascimento = models.CharField(max_length=10)
    endereco = models.CharField(max_length=255)
    senha = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nome} - CPF: {self.cpf}"


class Conta(models.Model):
    numero = models.IntegerField(unique=True)
    agencia = models.CharField(max_length=4, default='0001')
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)
    limite = models.DecimalField(max_digits=12, decimal_places=2, default=500.00)
    limite_saques = models.IntegerField(default=3)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='contas')

    def __str__(self):
        return f"Conta {self.numero} - {self.cliente.nome}"


class Transacao(models.Model):
    TIPO_CHOICES = (
        ('DEPOSITO', 'Depósito'),
        ('SAQUE', 'Saque'),
    )
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transacoes')
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.tipo} de R$ {self.valor} na conta {self.conta.numero}"
