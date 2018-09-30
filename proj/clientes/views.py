from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Cliente
from .forms import ClienteForm, SearchClienteForm
from django.contrib import messages

@login_required
def listarCliente(request, codigo=None):
    if codigo:
        cliente = get_object_or_404(Cliente, id=codigo)
        cliente_form = ClienteForm(instance=cliente)
        template = 'cliente_edit.html'
        context = { 'formEditar' : cliente_form , 'codigo':codigo }
    else:
        if request.method == 'POST':     #startwith contains
            form = SearchClienteForm(request.POST)
            query = request.POST.copy().get('query')
            clientes = Cliente.objects.all().filter(nome__contains=query).order_by('nome')
        else:                                          
            clientes = Cliente.objects.all().order_by('nome')
            form = SearchClienteForm()
        template = 'cliente_list.html'
        context = { 'clientes' : clientes , 'search': form}
    return render( request, template, context)

@login_required
def buscarCliente(request, query=None):
    clientes = Cliente.objects.all().filter(nome__contains=query).order_by('nome')
    template = 'cliente_list.html'
    context = { 'clientes' : clientes }
    return render( request, template, context)

@login_required
def editarCliente(request, codigo=None):
    tipo = messages.WARNING
    msg = 'Falha!'
    cliente = get_object_or_404(Cliente, id = codigo)
    new_data = ClienteForm(request.POST, instance=cliente) 
    if new_data.is_valid():
        if new_data.save():
            tipo = messages.SUCCESS
            msg = 'Cliente '+cliente.nome+' alterado com sucesso.'
        else:
            msg = 'Cliente '+cliente.nome+' não foi alterado.'
        
        messages.add_message(request, tipo , msg)
        return redirect('cliente_list')     
    else:
        return render( request, 'cliente_edit.html' , {'formEditar' : new_data, 'codigo':codigo })                

@login_required    
def cadastrarCliente(request):
    if request.method == 'POST':
        data = ClienteForm(request.POST) 
        if data.is_valid():
            if data.save():
                messages.add_message(request, messages.SUCCESS , 'Cliente cadastrado com sucesso.')
            else:
                messages.add_message(request, messages.WARNING , 'Falha no cadastro.')       
            return redirect('cliente_list') 
        else:
             return render( request, 'cliente_create.html', {'formCadastrar': data} )    
    else:    
        cadastrar_form = ClienteForm()
        return render( request, 'cliente_create.html', {'formCadastrar': cadastrar_form} )


     #return HttpResponseRedirect( reverse('cliente_details', kwargs={'codigo': 2}) )                
    #return render(request, 'cliente_list.html', {'clientes': Cliente.objects.all(), 'retorno':retorno, 'cliente_alterado': cliente.nome})
    #return render( request, 'cliente_edit.html', {'formEditar': new_data, 'retorno': False, 'cliente_old': cliente.nome })