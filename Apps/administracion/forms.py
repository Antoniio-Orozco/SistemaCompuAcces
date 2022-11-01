from django import forms
from .models import Proveedor,Producto

class ProveedorForm(forms.ModelForm):
    class Meta:
        model=Proveedor
        fields = ('nombre','telefono','direccion','nit')
        labels={
            'nombre' : 'Nombre Proveedor: ',
            'telefono' : 'Telefono: ',
            'direccion' : 'Dirección: ',
            'nit' : 'No. Nit:  '

        }

class EditarProveedorForm(forms.ModelForm):    
    class Meta:
        model=Proveedor
        fields = ('nombre','telefono','direccion','nit')
        labels={
            'nombre' : 'Nombre Proveedor: ',
            'telefono' : 'Telefono: ',
            'direccion' : 'Dirección: ',
            'nit' : 'No. Nit: '

        }
        widgets={
            'nombre' : forms.TextInput(attrs={'type':'text','id':'nombre_editar'}),
            'telefono' : forms.TextInput(attrs={'id':'telefono_editar'}),
            'direccion' : forms.TextInput(attrs={'id':'direccion_editar'}),
            'nit' : forms.TextInput(attrs={'id':'nit_editar'}),
        }

class ProductoForm(forms.ModelForm):
    class Meta:
        model=Producto
        fields = ('nombre','descripcion','categoria','cantidad','precio','icono','proveedor')
        labels={
            'nombre' : 'Nombre Producto: ',
            'descripcion' : 'Descripción: ',
            'categoria' : 'Categoría: ',
            'cantidad' : 'Cantidad:  ',
            'precio' : 'Precio: ',
            'icono' : 'Adjuntar Imagen:  ',
            'proveedor' : 'Proveedor: '
        }

class EditarProductoForm(forms.ModelForm):    
    class Meta:
        model=Producto
        fields = ('nombre','descripcion','cantidad','precio')
        labels={
            'nombre' : 'Nombre: ',
            'descripcion' : 'Descripcion: ',
            'cantidad' : 'Cantidad: ',
            'precio' : 'Precio: '

        }
        widgets={
            'nombre' : forms.TextInput(attrs={'type':'text','id':'nombre_editar'}),
            'descripcion' : forms.TextInput(attrs={'id':'descripcion_editar'}),
            'cantidad' : forms.NumberInput(attrs={'id':'cantidad_editar'}),
            'precio': forms.TextInput(attrs={'id':'precio_editar'}),
        }