from django.urls import path, re_path
from .views import listarCliente, editarCliente, cadastrarCliente,buscarCliente

urlpatterns = [
    path('', listarCliente , name='cliente_list'),
    path('cadastrar/' , cadastrarCliente , name='cliente_create'),
    path('<int:codigo>/', listarCliente  , name='cliente_details'),
    path('<int:codigo>/editar/' , editarCliente , name='cliente_edit'),
]

#Fluxo:request > urls > view > model > response