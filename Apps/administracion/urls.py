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
from .views import proveedor_view, productos_view, EditarProveedor_view, BorrarProveedor_view, EditarProducto_view,BorrarProducto_view
from Apps.administracion import views
from .views import CrearProveedor_view, CrearProducto_view
from django.contrib.auth.decorators import login_required

app_name='administracion'


urlpatterns = [
path('proveedor/', login_required(views.proveedor_view), name='proveedorapp'),
path('productos/', login_required(views.productos_view), name='productosapp'),


path('crearProveedor/',login_required(views.CrearProveedor_view), name='crearproveedor'),
path('crearProducto/',login_required(views.CrearProducto_view), name='crearproducto'),

path('editarProveedor/',login_required(views.EditarProveedor_view), name='editarproveedor'),
path('eliminarProveedor/<int:id_proveedor>',login_required(views.BorrarProveedor_view), name='eliminarproveedor'),

path('editarProducto/',login_required(views.EditarProducto_view), name='editarproducto'),
path('eliminarProducto/<int:id_producto>',login_required(views.BorrarProducto_view), name='eliminarproducto'),
]
