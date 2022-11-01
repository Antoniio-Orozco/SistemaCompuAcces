from django.contrib import admin
from .models import Cliente
# Register your models here.
class ClienteAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','nit')  
    search_fields=['nombre']
    filter_horizontal=()
    list_filter=()
    fieldsets=()

admin.site.register(Cliente,ClienteAdmin)