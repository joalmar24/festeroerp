from django.contrib import admin

# Register your models here.
from .models import Socio

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dni', 'email', 'estado', 'fecha_alta')
    search_fields = ('nombre', 'dni', 'email')
    list_filter = ('estado',)
