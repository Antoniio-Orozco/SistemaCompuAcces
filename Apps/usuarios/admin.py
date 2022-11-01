from django.contrib import admin
from .models import Empleado
# Register your models here.
class EmpleadoAdmin(admin.ModelAdmin):
    list_display=('nombre','apellido','tipo')  
    search_fields=['nombre']
    filter_horizontal=()
    list_filter=()
    fieldsets=()
    
admin.site.register(Empleado, EmpleadoAdmin)