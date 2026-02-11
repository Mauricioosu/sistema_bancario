from django.db import models
from django.contrib.auth.models import User


class Conta(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contas')
    numero = models.CharField(max_length=10, unique=True)
    agencia = models.CharField(max_length=4, default="0001")
    saldo = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    limite = models.DecimalField(max_digits=15, decimal_places=2, default=500.00)
    limite_saques = models.IntegerField(default=3)

    def __str__(self):
        return f"Conta {self.numero} - {self.usuario.username}"


class Transacao(models.Model):
    TIPO_CHOICES = [
        ('D', 'Depósito'),
        ('S', 'Saque'),
    ]
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transacoes')
    tipo = models.CharField(max_length=1, choices=TIPO_CHOICES)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} de R$ {self.valor}"
