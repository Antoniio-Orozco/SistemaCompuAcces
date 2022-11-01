from django.contrib import admin
from .models import Categoria, Proveedor , Producto

class ProveedorAdmin(admin.ModelAdmin):
    list_display=('nombre','direccion','nit')  
    search_fields=['nombre']
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Proveedor,ProveedorAdmin)

class ProductoAdmin(admin.ModelAdmin):
    list_display=('nombre','categoria','cantidad','precio')  
    search_fields=['nombre']
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Producto,ProductoAdmin)

admin.site.register(Categoria)

# Register your models here.

