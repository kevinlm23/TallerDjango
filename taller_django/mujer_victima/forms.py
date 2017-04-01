from django import forms
from models import *

class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ["nombre",
                  "email",
                  "sexo",
                  "telefono",
                  "creado_por",
                  "fecha_creacion"]