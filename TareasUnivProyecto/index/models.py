from datetime import datetime
from django.db import models

# Create your models here.
class CursosYTareas(models.Model):
    curso = models.CharField(max_length=100)
    tarea = models.CharField(max_length=100)
    valor = models.IntegerField()
    estado = models.CharField(max_length=100)
    entrega = models.DateField()
    usuario = models.CharField(default='usuario', max_length=100)

class EstadoDelCurso(models.Model):
    curso = models.CharField(max_length=100)
    estados=(
        ('1','pendiente'),
        ('2','verificado'),
        ('3','inexistente')
    )
    verificacion = models.CharField(max_length=30, default="pendiente", choices=estados)