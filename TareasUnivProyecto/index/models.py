import datetime
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

class EstadoDelCurso(models.Model):
    curso = models.CharField(max_length=100)
    verificacion = models.CharField(max_length=30, default="pendiente")