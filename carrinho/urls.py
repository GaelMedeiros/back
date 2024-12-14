from django.urls import path
from .views import addcarrinho, exibir_carrinho

urlpatterns = [
    path('addcarrinho/<int:produto_id>/', addcarrinho, name='addcarrinho'),
    path('', exibir_carrinho, name='exibir_carrinho'),

]