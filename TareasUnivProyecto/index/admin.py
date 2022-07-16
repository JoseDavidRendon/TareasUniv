from sqlite3 import Cursor
from django.contrib import admin
from index.models import CursosYTareas, EstadoDelCurso, Settings, Mensajes
# Register your models here.




class ModelCursosYtareas(admin.ModelAdmin):
    list_display=('usuario','curso', 'tarea', 'estado', 'id')
    list_filter = ('usuario', 'curso', 'estado')

class ModelEstadodelCurso(admin.ModelAdmin):
    list_display=('curso', 'verificacion')
    list_filter = ('curso', 'verificacion')

class ModelSettings(admin.ModelAdmin):
    list_display=('usuario',)
    list_filter = ('usuario',)

class ModelMensajes(admin.ModelAdmin):
    list_display=('para','de','asunto')
    list_filter = ('para','de')


admin.site.register(CursosYTareas, ModelCursosYtareas)
admin.site.register(EstadoDelCurso, ModelEstadodelCurso)
admin.site.register(Settings, ModelSettings)
admin.site.register(Mensajes, ModelMensajes)
