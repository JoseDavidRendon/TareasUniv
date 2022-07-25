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
    for tareas in CursosYTareas.objects.filter(usuario=usuario, curso = curso, calificado = True):
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
    notas_esperadas={}
    notas = {}
    notas_calificadas=0
    for materia in CursosYTareas.objects.filter(curso=curso, estado="terminada"):
        if materia.usuario in notas:
            notas_esperadas[materia.usuario]+=materia.valor
            notas[materia.usuario]+=materia.calificacion
        else:
            notas_esperadas[materia.usuario]=materia.valor
            notas[materia.usuario]=materia.calificacion
        if materia.usuario == request.user.username and materia.calificado==True:
            notas_calificadas+=materia.valor
    promedios=0
    for notass in notas:
        promedios+=(notas[notass]*100)/notas_esperadas[notass]
        
    promedio=(promedios/len(notas.keys()))
    personal_esperadas=notas_esperadas[request.user.username]
    personal=notas[request.user.username]
    promedioPersonal = (personal*100)/personal_esperadas
    # calificacion = round((notas[request.user.username]*5)/notas_esperadas[request.user.username],1)
    try:
        calificacion = round((notas[request.user.username]*5)/notas_calificadas,1)
    except:
        calificacion = 0
    error = 0
    if notas_esperadas[request.user.username]>500:
        error=1
    data={
        'promedioGlobal':int(promedio),
        'promedioPersonal':int(promedioPersonal),
        'calificacion':calificacion,
        'error':error
    }
    return (data)

@register.simple_tag
def pruebaa(val=None):
    data = {
        1:"hola",
        2:"adios"
    }
    return (data)

@register.simple_tag
def actualizarEstado(id):
    print("Visto",id)
    pass

@register.simple_tag
def calcularFecha(fecha):
    retornar=fecha-datetime.date.today()
    return  retornar.days