from django.db import models
from django.contrib.auth.models import User


class Conta(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    saldo = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Conta de {self.usuario.username}"


class Transacao(models.Model):
    TIPOS = (
        ('D', 'Depósito'),
        ('S', 'Saque'),
    )
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE, related_name='transacoes')
    tipo = models.CharField(max_length=1, choices=TIPOS)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.get_tipo_display()} - R$ {self.valor}"
