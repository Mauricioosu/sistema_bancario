from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('extrato/', views.extrato, name='extrato'),
    path('depositar/', views.depositar, name='depositar'),
    path('sacar/', views.sacar, name='sacar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),
]
