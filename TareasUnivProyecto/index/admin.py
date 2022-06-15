from sqlite3 import Cursor
from django.contrib import admin
from index.models import CursosYTareas, EstadoDelCurso
# Register your models here.


admin.site.register(CursosYTareas)
admin.site.register(EstadoDelCurso)
