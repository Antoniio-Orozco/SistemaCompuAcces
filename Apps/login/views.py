from email.mime import message
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from .forms import RegistroForm
from django.contrib import messages
from .models import Usuario
# Create your views here.

class loginview(TemplateView):
    template_name='index.html'

class HomeView(TemplateView):
    template_name='home.html'
    
def Login(request):
    if request.method=="POST":
       form=AuthenticationForm(request, data=request.POST)
       if form.is_valid():
        NombreUsuario=form.cleaned_data.get("username")
        contrasenia=form.cleaned_data.get("password")
        usuario=authenticate(username=NombreUsuario, password=contrasenia)
        if usuario is not None:
           login(request, usuario)
           return redirect("home/")
        else:
            messages.error(request,("usuario no valido"))
    else:
        messages.error(request,("No se pudo acceder"))

    form=AuthenticationForm()
    return render(request,"index.html",{"form":form})

def Logout(request):
    logout(request)
    messages.success(request,("Ha cerrado sesion"))
    return redirect("login:loginapp")

class RegistroView(CreateView):
    model=Usuario
    form_class=RegistroForm
    success_url= reverse_lazy('login:registro')