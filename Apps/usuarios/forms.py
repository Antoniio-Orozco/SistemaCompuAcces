from django import forms
from .models import  Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('nombre','apellido','telefono','tipo','disponibilidad')
        labels={
            'nombre' : 'Nombre Empleado: ',
            'apellido' : 'Apellido: ',
            'telefono' : 'Teléfono: ',
            'tipo':'Tipo de Empleado',
            'disponibilidad':'Disponibilidad del Empleado'
        }


class EditarEmpleadoForm(forms.ModelForm):
    class Meta:
        model=Empleado
        fields=('nombre','apellido','telefono','tipo','disponibilidad')
        labels={
            'nombre' : 'Nombre Empleado: ',
            'apellido' : 'Apellido: ',
            'telefono' : 'Teléfono: ',
            'tipo':'Tipo de Empleado',
            'disponibilidad':'Disponibilidad del Empleado'
        }
        widgets={
            'nombre' : forms.TextInput(attrs={'type':'text','id':'nombre_editar'}),
            'apellido' : forms.TextInput(attrs={'id':'apellido_editar'}),
            'telefono' : forms.TextInput(attrs={'id':'telefono_editar'}),
            'tipo':forms.TextInput(attrs={'id':'tipo_editar'}),
            'disponibilidad':forms.TextInput(attrs={'id':'disponibilidad_editar'}),
        }
