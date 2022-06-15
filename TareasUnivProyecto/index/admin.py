from sqlite3 import Cursor
from django.contrib import admin
from index.models import CursosYTareas, EstadoDelCurso
# Register your models here.




class ModelCursosYtareas(admin.ModelAdmin):
    list_display=('curso', 'tarea', 'estado')

class ModelEstadodelCurso(admin.ModelAdmin):
    list_display=('curso', 'verificacion')

admin.site.register(CursosYTareas, ModelCursosYtareas)
admin.site.register(EstadoDelCurso, ModelEstadodelCurso)
