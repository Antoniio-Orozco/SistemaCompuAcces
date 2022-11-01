from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, UpdateView
from .models import Cart, CartProducts, Venta
from .utils import getOrCreateCart, destroyCart
from .forms import VentaForm, VenForm
from Apps.administracion.models import Producto
from django.views.generic.detail import DetailView

class CrearClienteView(CreateView):
    template_name="clie.html"
    form_class=VenForm
    success_url= reverse_lazy('ventas:cart')

def cart(request): 
    cart = getOrCreateCart(request)
    return render(request, 'ventas.html',{'cart': cart})

def add(request):
    cart = getOrCreateCart(request)
    
    product = Producto.objects.get(pk = request.POST.get('product_id'))
    quantity = int(request.POST.get('quantity', 1))

    cart_product = CartProducts.objects.createOrUpdateQuantity(cart=cart, product=product , quantity=quantity)

    # cart.producto.add(product, through_defaults={
    #     'quantity':quantity
    # })

    # return render(request, 'agregar.html', {'product': product}) 
    return render(request, 'ventas.html',{'cart': cart})

def getOne(request):
    product = Producto.objects.get(pk = request.POST.get('product_id'))

    return render(request, 'agregar.html', {'product': product}) 

def remove(request):
    cart = getOrCreateCart(request)
    product = Producto.objects.get(pk = request.POST.get('product_id'))
    cart.producto.remove(product)

    return redirect('ventas:cart')

def complete(request):
    cart = getOrCreateCart(request)
    productos = Producto.objects.filter(nombre = cart.producto)
    venta = Venta.objects.create(empleado= cart.empleado,fecha = cart.fecha, total = cart.total, cliente=cart.cliente)
    venta.producto.set(cart.producto.all())
    
    destroyCart(request)

    return redirect('ventas:sales')

class VentasListView(ListView):
    template_name='sales.html'
    model = Venta

class AgregarCliente(UpdateView):
    template_name= "clie.html"
    model=Venta
    form_class = VenForm
    success_url = reverse_lazy('ventas:sales')

class detallesVenta(DetailView):
    template_name ='detallesVenta.html'
    queryset = Venta.objects.all()