from django.urls import path 
from .views import listar_estilos, cadastrar_estilos, editar_estilos, excluir_estilos

urlpatterns = [
    path('', listar_estilos, name = 'listar_estilo'), 
    path('cadastrar/', cadastrar_estilos, name = 'cadastrar_estilos'),
    path('editar/<int:id>/', editar_estilos, name= 'editar_estilos'),
    path('excluir/<int:id>', excluir_estilos, name = 'excluir_estilos')
]
