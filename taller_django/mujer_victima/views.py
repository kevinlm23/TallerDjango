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

class CrearRegistro(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = "crear_registro.html"

    def get_success_url(self):
        return reverse("home")