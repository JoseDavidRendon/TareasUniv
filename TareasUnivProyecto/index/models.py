from django.db import models

# Create your models here.
class materias (models.Model):
    Curso = models.CharField(max_length=100, null=False, blank=False)