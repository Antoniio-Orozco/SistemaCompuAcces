from django.shortcuts import render, redirect
from django.contrib import messages
from pyexpat.errors import messages
from .forms import ProveedorForm, ProductoForm, EditarProveedorForm, EditarProductoForm
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.http import HttpRequest
from django.views import generic
from django.db.models import Q
from .models import Producto, Proveedor

# Create your views here.

def productos_view(request):
    busqueda = request.GET.get("buscar")
    productos = Producto.objects.all()
    form_personal = ProductoForm()
    form_editar= EditarProductoForm()
    productos_count = Producto.objects.all().count()

    if busqueda:
        productos=Producto.objects.filter(
            Q(nombre__icontains = busqueda)| 
            Q(descripcion__icontains=busqueda)|
            Q(categoria__nombre__icontains=busqueda)                     
        ).distinct()

    context= {
        'productos': productos,
        'form_personal' : form_personal,
        'form_editar':form_editar,
        'productos_count': productos_count
    }
    return render(request,'products.html',context)

def CrearProducto_view(request):
    if request.POST:
        form = ProductoForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar el producto")    
                return redirect('administracion:productosapp')
    return redirect('administracion:productosapp')

def proveedor_view(request):
    busqueda = request.GET.get("buscar")
    proveedores = Proveedor.objects.all()
    form_personal = ProveedorForm()
    form_editar=EditarProveedorForm()
    proveedores_count = Proveedor.objects.all().count()

    if busqueda:
        proveedores=Proveedor.objects.filter(
            Q(nombre__icontains = busqueda)|
            Q(telefono__icontains=busqueda)|
            Q(nit__icontains=busqueda) 
        ).distinct()

    context= {
        'proveedores': proveedores,
        'form_personal' : form_personal,
        'form_editar':form_editar,
        'proveedores_count':proveedores_count
    }
    return render(request,'providers.html',context)



def CrearProveedor_view(request):
    if request.POST:
        form = ProveedorForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar el proveedor")    
                return redirect('administracion:proveedorapp')
    return redirect('administracion:proveedorapp')

def BorrarProveedor_view(request, id_proveedor):
    proveedor=Proveedor.objects.get(pk=id_proveedor)
    proveedor.delete()
    return redirect('administracion:proveedorapp')

def EditarProveedor_view(request):
    if request.POST:
        proveedor = Proveedor.objects.get(pk=request.POST.get('id_personal_editar'))
        form=EditarProveedorForm(request.POST, request.FILES, instance=proveedor)
        if form.is_valid():           
            form.save()           
    return redirect('administracion:proveedorapp')

def BorrarProducto_view(request, id_producto):
    producto=Producto.objects.get(pk=id_producto)
    producto.delete()
    return redirect('administracion:productosapp')

def EditarProducto_view(request):
    if request.POST:
        producto = Producto.objects.get(pk=request.POST.get('id_personal_editar'))
        form=EditarProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():           
            form.save()          
    return redirect('administracion:productosapp')