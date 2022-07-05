
import datetime
from pyexpat.errors import messages
from random import random
from urllib import request
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators  import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm, formAgregarCurso, formAnotaciones
from .models import CursosYTareas, EstadoDelCurso, Settings
from django import template
# Create your views here.

@login_required


def inicio(request):
    usuario = request.user.username
    formTareasPendientes = CursosYTareas.objects.filter(estado="espera", usuario = usuario)
    formTareasProceso = CursosYTareas.objects.filter(estado="proceso", usuario = usuario)
    formTareasTerminadas = CursosYTareas.objects.filter(estado="terminada", usuario = usuario)
    diasRestantes = []
    for tarea in formTareasPendientes:
        diaRestante= tarea.entrega - datetime.date.today()
        diasRestantes.append((tarea.id, diaRestante.days))
    diasRestantesProceso = []
    for tarea in formTareasProceso:
        diaRestante= tarea.entrega - datetime.date.today()
        diasRestantesProceso.append((tarea.id, diaRestante.days))
    data={
        'formTareasPendientes':formTareasPendientes,
        'formTareasProceso':formTareasProceso,
        'formTareasTerminadas':formTareasTerminadas,
        'diasRestantes':diasRestantes,
        'diasRestantesProceso':diasRestantesProceso,
        'formAnotaciones': formAnotaciones()
    } 
    return render(request, 'index/index.html', data)


def enviarAnotacion(request):
    return redirect(to=inicio)


def registro(request):
    error= False
    if request.method =='POST':
        formulario = UserRegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Profile details updated.')
            return redirect(to=inicio)
        else:
            #error=formulario.errors.as_data
            error = formulario.errors.values
    data={
        'form':UserRegisterForm(),
        'error':error
        }       
    return render(request, 'registration/registro.html', data)



def salir(request):
    logout()
    return redirect(to=inicio)



def agregarCurso(request):
    if request.method == 'POST':
        formulario = formAgregarCurso(request.POST)
        if formulario.is_valid():
            form=CursosYTareas()
            form.curso = formulario.cleaned_data['curso'].lower()
            form.estado = formulario.cleaned_data['estado']
            form.tarea = formulario.cleaned_data['tarea']
            form.valor = formulario.cleaned_data['valor']
            form.entrega = formulario.cleaned_data['entrega']
            #form.usuario = formulario.cleaned_data['usuario']
            form.usuario = request.user
            form.save()
            formEstadoDelCurso=EstadoDelCurso()
            Existencia = EstadoDelCurso.objects.filter(curso=formulario.cleaned_data['curso'].lower()).count()
            if Existencia == 0:
                formEstadoDelCurso.curso=formulario.cleaned_data['curso']
                formEstadoDelCurso.save()
                
            data={
                'form':formAgregarCurso(),
                'cursosVerificados': EstadoDelCurso.objects.filter(verificacion='verificado'),
                'error':False,
            }
            return render(request, 'index/AgregarCurso.html', data)
        else:
            
            data={
                'form':formAgregarCurso(),
                'cursosVerificados': EstadoDelCurso.objects.filter(verificacion='verificado'),
                'error':True,
            }
            return render(request, 'index/AgregarCurso.html', data)



def nuevoCurso(request):
    data={
        'form':formAgregarCurso(),
        'cursosVerificados': EstadoDelCurso.objects.filter(verificacion='verificado')
    }
    #cursos= EstadoDelCurso()
    #return HttpResponse(cursos)
    return render(request, 'index/AgregarCurso.html', data, )



@login_required
def editarTarea(request, id):
    usuario = request.user.username
    formInfo = CursosYTareas.objects.get(pk = id)
    if usuario == formInfo.usuario:
        data={
            'form':formAgregarCurso(instance=formInfo),
            'cursosVerificados': EstadoDelCurso.objects.filter(verificacion='verificado'),
            'id':id
        }
        return render(request, 'index/editarTarea.html', data)
    else:
        return HttpResponse("Error")


def actualizarCurso(request):
    if request.method == 'POST':
        id = int(request.POST['id'])
        formulario = formAgregarCurso(request.POST)
        if formulario.is_valid():
            form = CursosYTareas.objects.filter(id=id)
            if id==form[0].id:
                form.update(
                    curso=formulario.cleaned_data['curso'].lower(),
                    tarea=formulario.cleaned_data['tarea'],
                    valor=formulario.cleaned_data['valor'],
                    estado=formulario.cleaned_data['estado'],
                    entrega=formulario.cleaned_data['entrega']
                    )
                for object in form:
                    object.save()
                return redirect(to=inicio)
    
    return HttpResponse("Error")


def borrarCurso(request, id):
    username=request.user.username
    form = CursosYTareas.objects.get(pk=id)
    if form.usuario == username:
    #if request.method == 'GET':
        tarea = CursosYTareas.objects.filter(id=id)
        tarea.delete()
        return redirect(to=inicio)
    return HttpResponse("No puede eliminar un curso que no le pertenece.")

def actualizarAnotacion(request):
    usuario=request.user.username
    id=int((request.POST['id']))
    anotacion = request.POST['anotacion']
    form = CursosYTareas.objects.get(pk=id)
    if form.usuario == usuario:
        form.anotacion = anotacion
        form.save()
        return redirect(to=inicio)   

    return HttpResponse("no funciona")

@login_required
def dashboard(request):
    usuario = request.user.username
    tareas = CursosYTareas.objects.filter(usuario=usuario)
    try:
        config = Settings.objects.get(usuario=usuario)
        dashboardConfig = config.dashboardActivos.split(",")
        print( dashboardConfig)
    except:
        config = Settings.objects.create(usuario=usuario)
        dashboardConfig=("")
    cursos = []
    for curso in tareas:
        cursos.append(curso.curso)
    cursosSinRepetir=list(set(cursos))
    data={
        'tareas':tareas,
        'cursosDisponibles': dashboardConfig,
        'todosLosCursos':cursosSinRepetir
    }
    return render(request, 'index/dashboard.html', data)

def actualizarConfigDashboard(request):
    cursosSeleccionados=",".join([tarea for tarea in request.POST if tarea!='csrfmiddlewaretoken'])
    # print(cursosSeleccionados)
    abrirSettings, created = Settings.objects.get_or_create(
    usuario=request.user.username,
    defaults={'usuario':request.user.username, 'dashboardActivos':cursosSeleccionados}
    )
    if not created:
        abrirSettings.dashboardActivos = cursosSeleccionados
        abrirSettings.save()
    return redirect(to=dashboard)

def editarCalificado(request):
    estado = int(request.POST['check-value'])
    id = int(request.POST['id'])
    try:
        valor = int(request.POST['calif-tarea'])
    except:
        pass
    formTarea = formularioTareas = CursosYTareas.objects.get(pk=id)
    userId=  formTarea.usuario
    userLocal = request.user.username
    if (userLocal == userId):
        if (estado==1):
            formTarea.calificado=True
            formTarea.calificacion=valor
            formTarea.save()
        elif (estado ==0):
            formTarea.calificado=False
            formTarea.save()
        else:
            return HttpResponse('Error')        
    return redirect(to=inicio)

def traer_usuario(request):
    usuario=request.user.username
    print(usuario)
    return usuario