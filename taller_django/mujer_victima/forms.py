from django import forms
from models import *

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ["nombre",
                  "email",
                  "sexo",
                  "telefono",
                  "creado_por"]

class EstudioForm(forms.ModelForm):

    class Meta:
        model = Estudio
        fields = ["nombre",
                  "categoria",
                  "persona",
                  "finalizado",
                  "creado_por"]

class CasoViolenciaForm(forms.ModelForm):

    class Meta:
        model = CasoViolencia
        fields = ["descripcion",
                  "persona",
                  "fecha",
                  "nombre_agresor",
                  "creado_por"]