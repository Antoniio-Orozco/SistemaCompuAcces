from django.shortcuts import render,redirect
from django.contrib import messages
from pyexpat.errors import messages
from .forms import EmpleadoForm, EditarEmpleadoForm
from .models import Empleado
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView


def usuario_view(request):
    busqueda = request.GET.get("buscar")
    usuarios = Empleado.objects.all()
    form_empleado = EmpleadoForm()
    form_editar=EditarEmpleadoForm()
    empleados_count = Empleado.objects.all().count()
 
    if busqueda:
        usuarios=Empleado.objects.filter(
            Q(nombre__icontains = busqueda)|
            Q(apellido__icontains=busqueda)
        ).distinct()

    context= {
        'usuarios': usuarios,
        'form_empleado' : form_empleado,
        'form_editar':form_editar,
        'empleados_count':empleados_count
    }
    return render(request,'admin.html',context)

def CrearUsuario_view(request):
    if request.POST:
        form = EmpleadoForm(request.POST,request.FILES)
        if form.is_valid:
            try:
                form.save()
            except:
                messages(request, "Error al guardar empleado")    
                return redirect('usuarios:usuariosapp')
    return redirect('usuarios:usuariosapp')

def BorrarUsuario_view(request, id_usuario):
    usuario=Empleado.objects.get(pk=id_usuario)
    usuario.delete()
    return redirect('usuarios:usuariosapp')

def EditarUsuario_view(request):
    if request.POST:
        usuario = Empleado.objects.get(pk=request.POST.get('id_personal_editar'))
        form=EditarEmpleadoForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid:           
            form.save()           
    return redirect('usuarios:usuariosapp')

