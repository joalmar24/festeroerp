from django.contrib import admin
# Register your models here.
from .models import Socio, TipoSocio, Condicion
from .forms import SocioForm

#@admin.register(TipoSocio)
#class TipoAdmin(admin.ModelAdmin):
#    list_display = ('nombre',)
class CondicionInline(admin.TabularInline):
    model = Condicion
    extra = 1

@admin.register(TipoSocio)
class TipoAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    inlines = [CondicionInline]

@admin.register(Condicion)
class CondicionAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo')
    search_fields = ('nombre',)
    list_filter = ('tipo',)

@admin.register(Socio)
class SocioAdmin(admin.ModelAdmin):
    form = SocioForm
    list_display = ('numero_festero', 'nombre', 'tipo', 'condicion', 'estado')
    list_filter = ('tipo', 'estado')
    search_fields = ('nombre', 'dni')
    autocomplete_fields = ['condicion']
    date_hierarchy = 'fecha_alta'
    list_editable = ('estado',)
    ordering = ('numero_festero',)

#@admin.register(Socio)
#class SocioAdmin(admin.ModelAdmin):
#    list_display = ('nombre', 'dni', 'email', 'estado', 'fecha_alta')
#    search_fields = ('nombre', 'dni', 'email')
#    list_filter = ('estado',)
