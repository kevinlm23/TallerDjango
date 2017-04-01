from django.conf.urls import patterns, url
from mujer_victima.views import *

urlpatterns = [
    url(r'^$',home, name = 'home'),
    url(r'^crear/$', CrearRegistro.as_view(), name='crear_registro'),
]
