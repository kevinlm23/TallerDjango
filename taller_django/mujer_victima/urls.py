from django.conf.urls import patterns, url
from mujer_victima.views import *

urlpatterns = [
    url(r'^$',home, name = 'home'),
    url(r'^crear/$', CrearPersona.as_view(), name='crear_persona'),
    url(r'^lista_personas/$', ListaPersonas.as_view(), name='lista_personas'),

    url(r'^lista_actualizar/$', ListaActualizarPersona.as_view(), name='lista_actualizar_persona'),
    url(r'^actualizar_persona/(?P<pk>\d+)/$', ActualizarPersona.as_view(), name='actualizar_persona'),

    url(r'^lista_eliminar/$', ListaEliminarRegistro.as_view(), name='lista_eliminar_registro'),
    url(r'^eliminar_registro/(?P<pk>\d+)/$', EliminarRegistro.as_view(), name='eliminar_registro'),
]
