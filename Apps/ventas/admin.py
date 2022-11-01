from django.contrib import admin
from .models import Cart
# Register your models here.

from .models import Cart, Venta, CartProducts
# Register your models here.

admin.site.register(Venta)
admin.site.register(CartProducts)