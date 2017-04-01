from django.conf.urls import patterns, url
from mujer_victima.views import *

urlpatterns = [
    url(r'^$',home, name = 'home'),
    url(r'^crear/$', CrearPersona.as_view(), name='crear_persona'),
    url(r'^crear_estudio/$', CrearEstudio.as_view(), name='crear_estudio'),
    url(r'^crear_caso/$', CrearCasoViolencia.as_view(), name='crear_caso'),
    url(r'^lista_personas/$', ListaPersonas.as_view(), name='lista_personas'),
    url(r'^detalle_persona/(?P<pk>\d+)/$', DetallePersona.as_view(), name='detalle_persona'),
    url(r'^detalle_caso/(?P<pk>\d+)/$', DetalleViolencia.as_view(), name='detalle_caso'),
    url(r'^detalle_estudio/(?P<pk>\d+)/$', DetalleEstudio.as_view(), name='detalle_estudio'),

    url(r'^lista_actualizar/$', ListaActualizarPersona.as_view(), name='lista_actualizar_persona'),
    url(r'^actualizar_persona/(?P<pk>\d+)/$', ActualizarPersona.as_view(), name='actualizar_persona'),

    url(r'^lista_eliminar/$', ListaEliminarRegistro.as_view(), name='lista_eliminar_registro'),
    url(r'^eliminar_registro/(?P<pk>\d+)/$', EliminarRegistro.as_view(), name='eliminar_registro'),
]
