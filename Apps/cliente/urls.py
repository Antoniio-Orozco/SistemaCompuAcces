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
from .views import clientes_view, CrearCliente_view, BorrarCliente_view, EditarCliente_view
from Apps.cliente import views
from django.contrib.auth.decorators import login_required

app_name='cliente'

urlpatterns = [
path('', login_required(views.clientes_view), name='clientesapp'),
path('crearCliente/', login_required(views.CrearCliente_view), name='crearcliente'),
path('eliminarCliente/<int:id_cliente>', login_required(views.BorrarCliente_view), name='eliminarcliente'),
path('editarCliente/', login_required(views.EditarCliente_view), name='editarcliente'),
]   
