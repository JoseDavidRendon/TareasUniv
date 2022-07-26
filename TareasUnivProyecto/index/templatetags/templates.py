from audioop import avg
from django import template
from ..models import CursosYTareas, EstadoDelCurso, Settings, Mensajes
import json
from django.utils.safestring import SafeString
from django.template.defaultfilters import stringfilter
from django.db.models import Avg, Min
from django.contrib.auth.models import User
import datetime
import time
register = template.Library()

@register.simple_tag
def obtenerProgreso(request, curso):
    usuario = request.user.username
    retornar= 0
    for tareas in CursosYTareas.objects.filter(usuario=usuario, curso = curso, calificado = True, estado='terminada'):
        retornar+=tareas.valor 
    return (retornar)#valor 0-500

@register.simple_tag
def obtenerValoresDeCalificacion(request, curso):
    usuario = request.user.username
    positivo = 0
    negativo  = 0
    pendiente = 0
    for tareas in CursosYTareas.objects.filter(curso = curso, usuario=usuario, estado='terminada'):
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
    for tareas in CursosYTareas.objects.filter(usuario=usuario, curso=curso, estado="terminada", calificado=True).order_by('entrega'):
        datos["Tarea %s" %paso]={"nombre":tareas.tarea,
        "calificacion":round(((tareas.calificacion*100)/tareas.valor))
        }
        paso +=1
    datos_json = json.dumps(datos)
    return(datos_json)

@register.simple_tag
def comprobarCheckedDB(request, id):
    usuario= request.user.username
    tarea = Settings.objects.get(usuario=usuario)
    listaTareas=(tarea.dashboardActivos).split(",")
    if id in listaTareas:
        return 1
    else:
        return 0

@register.simple_tag
def obtenePromedioDelCurso(request, curso):
    error=0
    todosUsuarios = CursosYTareas.objects.filter(curso=curso, estado='terminada', calificado=True)
    notasTodos={}
    for usuar in todosUsuarios.values_list('usuario', flat=True):
        usuarMax=todosUsuarios.filter(usuario=usuar).values_list('valor', flat=True)
        usuarProm=todosUsuarios.filter(usuario=usuar).values_list('calificacion', flat=True)
        notasTodos[usuar]=(sum(usuarProm)*5)/sum(usuarMax)        
    promedio=0
    promedioPersonal = 0
    calificacion=0
    if len(notasTodos)>0:
        promedio = (sum(notasTodos.values())/len(notasTodos.values()))
    if request.user.username in notasTodos.keys():
        promedioPersonal=(notasTodos[request.user.username]*100)/5
        calificacion=round(notasTodos[request.user.username],1)
    if sum(todosUsuarios.filter(usuario=request.user.username).values_list('valor', flat=True))>500:
        error=1

    data={
        'promedioGlobal':int((promedio*100)/5),
        'promedioPersonal':int(promedioPersonal),
        'calificacion':calificacion,
        'error':error
    }
    return (data)

@register.simple_tag
def calcularFecha(fecha):
    retornar=fecha-datetime.date.today()
    return  retornar.days