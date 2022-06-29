from django import template
from ..models import CursosYTareas, EstadoDelCurso
register = template.Library()

@register.simple_tag
def obtenerProgreso(request, curso):
    usuario = request.user.username
    retornar= 0
    for tareas in CursosYTareas.objects.filter(usuario=usuario, curso = curso):
        retornar+=tareas.valor 
    return (retornar)#valor 0-500

@register.simple_tag
def obtenerProgresoVerde(request, curso):
    usuario = request.user.username
    porcentajeVerde = 0
    porcentajeAmarillo = 0
    for tareas in CursosYTareas.objects.filter(usuario=usuario, curso = curso):
        if tareas.calificado:
            porcentajeVerde+=tareas.calificacion
    return(porcentajeVerde)

@register.simple_tag
def obtenerProgresoAmarillo(request, curso):
    usuario = request.user.username
    porcentajeAmarillo = 0
    for tareas in CursosYTareas.objects.filter(usuario=usuario, curso = curso):
        porcentajeAmarillo += tareas.valor
    return(porcentajeAmarillo)

@register.simple_tag
def obtenerProgresoRojo(request, curso):
    usuario = request.user.username
    valorCalificado = 0
    for tareas in CursosYTareas.objects.filter(usuario=usuario, curso = curso):
        if tareas.calificado:
            valorCalificado += tareas.valor
    print(valorCalificado)
    return(valorCalificado)

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
