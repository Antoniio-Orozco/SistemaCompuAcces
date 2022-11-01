"""SistemaCompuAcces URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.auth.decorators import login_required

app_name='ventas'

urlpatterns = [
path('agregarcliente/ <int:pk>/',login_required(views.AgregarCliente.as_view()), name='agregarcl'),
path('carrito/',login_required(views.cart) , name='cart'),
path('carrito/agregar/',login_required(views.add) , name='add'),
path('carrito/eliminar/',login_required(views.remove), name='remove'),
path('listarVenta/', login_required(views.VentasListView.as_view()), name='sales'),
path('completar/',login_required(views.complete), name='complete'),
path('producto/',login_required(views.getOne), name='getOne'),
path('detallesVenta/ <int:pk>/',login_required(views.detallesVenta.as_view()), name='detallesVenta'),
]
