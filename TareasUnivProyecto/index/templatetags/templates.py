from django import template
from ..models import CursosYTareas, EstadoDelCurso, Settings
import json
from django.utils.safestring import SafeString
from django.template.defaultfilters import stringfilter
register = template.Library()

@register.simple_tag
def obtenerProgreso(request, curso):
    usuario = request.user.username
    retornar= 0
    for tareas in CursosYTareas.objects.filter(usuario=usuario, curso = curso):
        retornar+=tareas.valor 
    return (retornar)#valor 0-500

@register.simple_tag
def obtenerValoresDeCalificacion(request, curso):
    usuario = request.user.username
    positivo = 0
    negativo  = 0
    pendiente = 0
    for tareas in CursosYTareas.objects.filter(curso = curso, usuario=usuario):
        if tareas.calificado:
            positivo += tareas.calificacion
            negativo += tareas.valor-tareas.calificacion
        else:
            pendiente += tareas.valor
    datos="{0},{1},{2}".format(positivo, negativo, pendiente)
    return datos

@register.simple_tag
def obtenerValoresGraficaLineal(request, curso):
    usuario = request.user.username
    datos={}
    paso=1
    for tareas in CursosYTareas.objects.filter(usuario=usuario, curso=curso, estado="terminada", calificado=True):
        datos["Tarea %s" %paso]={"nombre":tareas.tarea,
        "calificacion":int(((tareas.calificacion*100)/tareas.valor))
        }
        paso +=1
    datos_json = json.dumps(datos)
    return(datos_json)

@register.simple_tag
def comprobarCheckedDB(request, id):
    usuario= request.user.username
    tarea = Settings.objects.get(usuario=usuario)
    listt = tarea.dashboardActivos
    listtt = listt.lower()
    listaTareas=listt.split(",")
    if id.lower() in listaTareas:
        return 1
    else:
        return 0