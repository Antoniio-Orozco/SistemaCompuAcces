from django.shortcuts import render,redirect
from django.contrib import messages
from pyexpat.errors import messages
from .forms import ClienteForm, EditarClienteForm
from .models import Cliente
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

def clientes_view(request):
    busqueda = request.GET.get("buscar")
    clientes = Cliente.objects.all()
    form_personal = ClienteForm()
    form_editar=EditarClienteForm()
    clientes_count = Cliente.objects.all().count()

    if busqueda:
        clientes=Cliente.objects.filter(
            Q(nombre__icontains = busqueda)|
            Q(apellido__icontains=busqueda)|
            Q(nit__icontains=busqueda) 
        ).distinct()

    context= {
        'clientes': clientes,
        'form_personal' : form_personal,
        'form_editar': form_editar,
        'clientes_count' : clientes_count
    }

    

    return render(request,'client.html',context)

def CrearCliente_view(request):
    if request.POST:
        form = ClienteForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar el cliente")    
                return redirect('cliente:clientesapp')
    return redirect('cliente:clientesapp')

def BorrarCliente_view(request, id_cliente):
    cliente=Cliente.objects.get(pk=id_cliente)
    cliente.delete()
    return redirect('cliente:clientesapp')

def EditarCliente_view(request):
    if request.POST:
        cliente = Cliente.objects.get(pk=request.POST.get('id_personal_editar'))
        form=EditarClienteForm(request.POST, request.FILES, instance=cliente)
        if form.is_valid:           
            form.save()           
    return redirect('cliente:clientesapp')

# Create your views here.
