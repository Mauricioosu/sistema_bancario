from rest_framework import serializers
from .models import Cliente, Conta, Transacao


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['id', 'nome', 'cpf', 'data_nascimento', 'endereco']


class ContaSerializer(serializers.ModelSerializer):
    cliente_detalhes = ClienteSerializer(source='cliente', read_only=True)

    class Meta:
        model = Conta
        fields = ['id', 'numero', 'agencia', 'saldo', 'limite', 'limite_saques', 'cliente', 'cliente_detalhes']
        read_only_fields = ['saldo']


class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['id', 'tipo', 'valor', 'data', 'conta']
        read_only_fields = ['data']


class OperacaoBancariaSerializer(serializers.Serializer):
    numero_conta = serializers.IntegerField()
    valor = serializers.DecimalField(max_digits=12, decimal_places=2)

    def validate_valor(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor da operação deve ser maior que zero.")
        return value
