from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Cliente, Conta, Transacao


class ClienteSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})

    class Meta:
        model = Cliente
        fields = ['id', 'username', 'password', 'nome', 'cpf', 'data_nascimento', 'endereco']

    def create(self, validated_data):
        username = validated_data.pop('username')
        password = validated_data.pop('password')

        user = User.objects.create_user(
            username=username,
            password=password
        )

        cliente = Cliente.objects.create(
            usuario=user,
            **validated_data
        )
        return cliente


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
