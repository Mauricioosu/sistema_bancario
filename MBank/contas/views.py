from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cliente, Conta, Transacao
from .serializers import (
    ClienteSerializer,
    ContaSerializer,
    TransacaoSerializer,
    OperacaoBancariaSerializer
)
from .services import ContaService


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class ContaViewSet(viewsets.ModelViewSet):
    serializer_class = ContaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):

        user = self.request.user
        if user.is_superuser:
            return Conta.objects.all()
        return Conta.objects.filter(cliente__usuario=user)

    @action(detail=True, methods=['post'])
    def depositar(self, request, pk=None):
        conta = self.get_object()
        serializer = OperacaoBancariaSerializer(data=request.data)
        if serializer.is_valid():
            valor = serializer.validated_data['valor']
            try:
                novo_saldo = ContaService.depositar(conta, valor)
                return Response({"mensagem": "Depósito realizado com sucesso.", "novo_saldo": novo_saldo}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def sacar(self, request, pk=None):
        conta = self.get_object()
        serializer = OperacaoBancariaSerializer(data=request.data)
        # ... (restante código do sacar igual ao anterior)
        if serializer.is_valid():
            valor = serializer.validated_data['valor']
            try:
                novo_saldo = ContaService.sacar(conta, valor)
                return Response({"mensagem": "Saque realizado com sucesso.", "novo_saldo": novo_saldo}, status=status.HTTP_200_OK)
            except ValueError as e:
                return Response({"erro": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TransacaoViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TransacaoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Transacao.objects.all().order_by('-data')
        return Transacao.objects.filter(conta__cliente__usuario=user).order_by('-data')
