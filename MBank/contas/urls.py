from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ContaViewSet, TransacaoViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet)
router.register(r'contas', ContaViewSet)
router.register(r'transacoes', TransacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
