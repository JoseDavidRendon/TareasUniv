from sqlite3 import Cursor
from django.contrib import admin
from index.models import CursosYTareas, EstadoDelCurso
# Register your models here.




class ModelCursosYtareas(admin.ModelAdmin):
    list_display=('usuario','curso', 'tarea', 'estado')
    list_filter = ('usuario', 'curso', 'estado')

class ModelEstadodelCurso(admin.ModelAdmin):
    list_display=('curso', 'verificacion')
    list_filter = ('curso', 'verificacion')

admin.site.register(CursosYTareas, ModelCursosYtareas)
admin.site.register(EstadoDelCurso, ModelEstadodelCurso)
