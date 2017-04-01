from django.shortcuts import render
from models import *
from forms import *
from django.core.urlresolvers import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    return render(request,'inicio.html')

############ CREAR

class CrearPersona(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "crear_persona.html"

    def get_success_url(self):
        return reverse("lista_personas")

class CrearEstudio(CreateView):
    model = Estudio
    form_class = EstudioForm
    template_name = "crear_persona.html"

    def get_success_url(self):
        return reverse("lista_personas")

class CrearCasoViolencia(CreateView):
    model = CasoViolencia
    form_class = CasoViolenciaForm
    template_name = "crear_caso.html"

    def get_success_url(self):
        return reverse("lista_personas")


#### LISTADO

class ListaPersonas(ListView):
    model = Persona
    template_name = "lista_personas.html"
    page_title = "Lista de Personas"
    sub_title = "Listado de Personas"
    estado = "0"

    def get_context_data(self, **kwargs):
        context = super(ListaPersonas, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['sub_title'] = self.sub_title
        context['estado'] = self.estado
        return context

########### ACTUALIZAR

class ActualizarPersona(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = "actualizar_persona.html"

    def get_success_url(self):
        return reverse("lista_personas")

class ListaActualizarPersona(ListView):
    model = Persona
    template_name = "lista_personas.html"
    page_title = "Actualizar una Persona"
    sub_title = "Actualizar Personas"
    estado = "1"

    def get_context_data(self, **kwargs):
        context = super(ListaActualizarPersona, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['estado'] = self.estado
        context['sub_title'] = self.sub_title
        return context

############ ELIMINAR

class ListaEliminarRegistro(ListView):
    model = Persona
    template_name = "lista_personas.html"
    page_title = "Eliminar una Registros"
    sub_title = "Eliminar Registros"
    estado = "2"

    def get_context_data(self, **kwargs):
        context = super(ListaEliminarRegistro, self).get_context_data(**kwargs)
        context['page_title'] = self.page_title
        context['estado'] = self.estado
        context['sub_title'] = self.sub_title
        return context

class EliminarRegistro(DeleteView):
    model = Persona
    form_class= PersonaForm
    template_name = "eliminar_registro.html"

    def get_success_url(self):
        return reverse("lista_personas")


######### DETALLE

class DetallePersona(DetailView):
    model = Persona
    template_name = "detalle_persona.html"
    estado="0"

    def get_context_data(self, **kwargs):
        context = super(DetallePersona, self).get_context_data(**kwargs)
        context['estado'] = self.estado
        return context

class DetalleViolencia(DetailView):
    model = CasoViolencia
    template_name = "detalle_persona.html"
    estado = "1"

    def get_context_data(self, **kwargs):
        context = super(DetalleViolencia, self).get_context_data(**kwargs)
        context['estado'] = self.estado
        return context

class DetalleEstudio(DetailView):
    model = Estudio
    template_name = "detalle_persona.html"
    estado = "2"

    def get_context_data(self, **kwargs):
        context = super(DetalleEstudio, self).get_context_data(**kwargs)
        context['estado'] = self.estado
        return context
