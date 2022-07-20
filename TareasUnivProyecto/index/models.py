import datetime
from django.forms import ImageField
import django.utils.timezone
from django.db import models

# Create your models here.
class CursosYTareas(models.Model):
    curso = models.CharField(max_length=100)
    tarea = models.CharField(max_length=100)
    valor = models.IntegerField()
    estado = models.CharField(max_length=100)
    entrega = models.DateField(default=django.utils.timezone.now)
    usuario = models.CharField(default='usuario', max_length=100)
    anotacion = models.TextField(default="", max_length=10000)
    calificado = models.BooleanField(default=False)
    calificacion = models.IntegerField(default=0)

class EstadoDelCurso(models.Model):
    curso = models.CharField(max_length=100)
    verificacion = models.CharField(max_length=30, default="pendiente")

class Settings(models.Model):
    usuario = models.CharField(default='usuario', max_length=100)
    dashboardActivos = models.TextField(default="none", max_length=9999999, null=True, blank=True)

class Mensajes(models.Model):
    para = models.CharField(default='usuario', max_length=100)
    de = models.CharField(default='Anonimo', max_length=100)
    asunto = models.CharField(default='Sin asunto', max_length=100)
    contenido = models.TextField(default="Mensjae vacío", max_length=9999999, null=True, blank=True)
    leido = models.BooleanField(default=False)
    fecha = models.DateField(default=django.utils.timezone.now)
