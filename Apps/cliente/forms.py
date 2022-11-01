from django import forms
from .models import Cliente


class ClienteForm(forms.ModelForm):
    class Meta:
        model=Cliente
        fields = ('nombre','apellido','nit','telefono')
        labels={
            'nombre' : 'Nombre Cliente: ',
            'apellido' : 'Apellido: ',
            'nit' : 'Nit Cliente: ',
            'telefono' : 'Teléfono: '

        }

class EditarClienteForm(forms.ModelForm):    
    class Meta:
        model=Cliente
        fields = ('nombre','apellido','nit','telefono')
        labels={
            'nombre' : 'Nombre Cliente: ',
            'apellido' : 'Apellido: ',
            'nit' : 'Nit Cliente: ',
            'telefono' : 'Teléfono: '

        }
        widgets={
            'nombre' : forms.TextInput(attrs={'type':'text','id':'nombre_editar'}),
            'apellido' : forms.TextInput(attrs={'id':'apellido_editar'}),
            'nit' : forms.TextInput(attrs={'id':'nit_editar'}),
            'telefono' : forms.TextInput(attrs={'id':'telefono_editar'}),
        }