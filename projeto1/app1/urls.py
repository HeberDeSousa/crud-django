from django.urls import path
from .views import index, create, read, update, delete

urlpatterns = [
    path('', index, name='indexUsuario'),
    path('criar/', create, name='criarUsuario'),
    path('visualizar/<int:user_id>', read, name='visualizarUsuario'),
    path('atualizar/<int:user_id>', update, name='atualizarUsuario'),
    path('apagar/<int:user_id>', delete, name='apagarUsuario'),
]
