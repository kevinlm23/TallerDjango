from django.contrib import admin
from models import *
# Register your models here.

class PersonaAdmin(admin.ModelAdmin):
    search_fields = ['nombre','email']
    list_display = ('nombre','email','sexo','telefono')
    fieldsets = (
        ("Informacion", {
            'fields': ('nombre','email','sexo','telefono','creado_por','fecha_creacion')
        }),
    )

class EstudioAdmin(admin.ModelAdmin):
    search_fields = ['nombre','persona','categoria']
    list_display = ('nombre','categoria','persona','finalizado')
    fieldsets = (
        ("Informacion", {
            'fields': ('nombre','categoria','persona','finalizado','creado_por','fecha_creacion')
        }),
    )

class CasoViolenciaAdmin(admin.ModelAdmin):
    search_fields = ['nombre_agresor','persona']
    list_display = ('descripcion','persona','fecha','nombre_agresor')
    fieldsets = (
        ("Informacion", {
            'fields': ('descripcion','persona','fecha','nombre_agresor','creado_por','fecha_creacion')
        }),
    )

admin.site.register(Persona, PersonaAdmin)
admin.site.register(Estudio, EstudioAdmin)
admin.site.register(CasoViolencia, CasoViolenciaAdmin)