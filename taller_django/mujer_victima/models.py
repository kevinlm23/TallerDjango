from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
import datetime

# Create your models here.

GENEROS_CHOICES = ('F', 'Femenino'),('M','Masculino')

class Persona(models.Model):
   nombre = models.CharField(max_length=200, verbose_name='Nombre', null=False, blank=False)
   email = models.EmailField(max_length=100, verbose_name='Email', null=False, blank=False)
   sexo = models.CharField(max_length=1, choices=GENEROS_CHOICES, verbose_name='Sexo',null=False, blank=False )
   telefono = models.IntegerField(verbose_name='Telefono', null=True, blank=True)
   creado_por = models.ForeignKey(User, null=False, blank=False, verbose_name='Creado_Por')
   fecha_creacion = models.DateTimeField(verbose_name='Fecha_Creacion', null=False, blank=False, default=datetime.datetime.now()
)

   class Meta:
       verbose_name = 'Persona'
       verbose_name_plural = 'Personas'

   def __unicode__(self):
       return self.nombre

   def save(self, *args, **kwargs):
       return super(Persona, self).save(*args, **kwargs)

   def get_absolute_url(self):
       view = "actualizar_persona"
       return reverse(view, kwargs={"pk": self.id})

   def get_success_url(self):
       view = "eliminar_registro"
       return reverse(view, kwargs={"pk": self.id})

class Estudio(models.Model):
   nombre = models.CharField(max_length=100, verbose_name='Nombre',null=False, blank=False)
   categoria = models.CharField(max_length=20, verbose_name='Categoria', null=False, blank=False)
   persona = models.ForeignKey(Persona, verbose_name='Persona', null=False, blank=False)
   finalizado = models.BooleanField(default=False, verbose_name='Finalizado', null=False, blank=False)
   creado_por = models.ForeignKey(User, null=False, blank=False, verbose_name='Creado_Por')
   fecha_creacion = models.DateTimeField(verbose_name='Fecha_Creacion', null=False, blank=False)

   class Meta:
       verbose_name = 'Estudio'
       verbose_name_plural = 'Estudios'

   def __unicode__(self):
       return self.nombre

   def save(self, *args, **kwargs):
       return super(Estudio, self).save(*args, **kwargs)

class CasoViolencia(models.Model):
   descripcion = models.TextField(max_length=200, verbose_name='Descripcion', null=False, blank=False,)
   persona = models.OneToOneField(Persona, verbose_name='Persona', null=False, blank=False,)
   fecha = models.DateField(verbose_name='Fecha', null=False, blank=False,)
   nombre_agresor = models.CharField(max_length=30, verbose_name='Nombre_Agresor', null=True, blank=True,)
   creado_por = models.ForeignKey(User, null=False, blank=False, verbose_name='Creado_Por')
   fecha_creacion = models.DateTimeField(verbose_name='Fecha_Creacion', null=False, blank=False)

   class Meta:
       verbose_name = 'Caso_Violencia'
       verbose_name_plural = 'Casos_Violencia'

   def __unicode__(self):
       return self.descripcion

   def save(self, *args, **kwargs):
       return super(CasoViolencia, self).save(*args, **kwargs)



