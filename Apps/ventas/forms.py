from django import forms
from .models import Cart, Venta

class VentaForm(forms.ModelForm):
    class Meta:
        model=Cart
        fields = '__all__'

class VenForm(forms.ModelForm):
    class Meta:
        model=Venta
        fields = ('cliente',)
