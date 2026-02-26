from django.contrib import admin

# Register your models here.
from .models import Socio, TipoSocio, Condicion

@admin.register(TipoSocio)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)

@admin.register(Condicion)
class CondicionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    list_filter = ('tipo',)

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'email', 'estado', 'fecha_alta')
    search_fields = ('nombre', 'dni', 'email')
    list_filter = ('estado',)
