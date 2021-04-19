from django.urls import path

from .views import ClienteView, ClienteCadastroView, ClienteUpdateView, ClienteDeleteView

urlpatterns = [
    path('clientes', ClienteView.as_view(), name='clientes'),
    path('cliente_add', ClienteCadastroView.as_view(), name='cliente_add'),
    path('cliente/<int:pk>/update', ClienteUpdateView.as_view(), name='cliente_upd'),
    path('cliente/<int:pk>/delete', ClienteDeleteView.as_view(), name='cliente_del'),
]
