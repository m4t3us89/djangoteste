from django.shortcuts import render
from .models import Produto
# Create your views here.
import datetime
def home(request):
    nome = 'Allisson Mateus Melo Reis'
    teste = datetime.datetime.now()
    #produto = Produto.objects.get(id=2) Pega Produto de id=2
    produtos = Produto.objects.all() #pega todos os produtos do banco
    return render(request, 'produtos.html', {'nome':nome, 'produtos':produtos , 'teste': teste})

def produto(request, codigo):
    produto = Produto.objects.get(id=codigo)
    return render(request, 'produtos.html', {'produto':produto})