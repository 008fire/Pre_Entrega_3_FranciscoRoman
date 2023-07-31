from django.contrib import admin
from django.urls import path

from App_control.views import (
    listar_articulos, crear_articulos, buscar_articulos, eliminar_articulos,
    editar_articulos, deliveryListView, deliveryCreateView,
    deliveryDetailView, deliveryUpdateView, deliveryDeleteView,clienteListView, clienteCreateView,
    clienteDetailView, clienteUpdateView, clienteDeleteView
)

urlpatterns = [
    # URLS de articulos
    path("articulos/", listar_articulos, name="lista_articulos"),
    path("crear-articulos/", crear_articulos, name="crear_articulos"),
    path("buscar-articulos/", buscar_articulos, name="buscar_articulos"),
    path("editar-articulos/<int:id>/", editar_articulos, name="editar_articulos"),
    path('eliminar-articulos/<int:id>/', eliminar_articulos, name="eliminar_articulos"),
    # URLS de deliverys
    path("delivery/", deliveryListView.as_view(), name="lista_delivery"),
    path('delivery/<int:pk>/', deliveryDetailView.as_view(), name="ver_delivery"),
    path('crear-delivery/', deliveryCreateView.as_view(), name="crear_delivery"),
    path('editar-delivery/<int:pk>/', deliveryUpdateView.as_view(), name="editar_delivery"),
    path('eliminar-delivery/<int:pk>/', deliveryDeleteView.as_view(), name="eliminar_delivery"),
    # URLS de clientes
    path("cliente/", clienteListView.as_view(), name="lista_cliente"),
    path('cliente/<int:pk>/', clienteDetailView.as_view(), name="ver_cliente"),
    path('crear-cliente/', clienteCreateView.as_view(), name="crear_cliente"),
    path('editar-cliente/<int:pk>/', clienteUpdateView.as_view(), name="editar_cliente"),
    path('eliminar-cliente/<int:pk>/', clienteDeleteView.as_view(), name="eliminar_cliente"),
]

