import datetime
from pyexpat.errors import messages
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators  import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm, formAgregarCurso, formAnotaciones,formReporte
from .models import CursosYTareas, EstadoDelCurso, Settings, Mensajes
from django.conf import settings
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
import time
# Create your views here.

@login_required


#view index, página principal
def inicio(request):
    inicio = time.time()
    usuario = request.user.username
    
    #llamada a la base de datos para obtener las tareas que se mostratán en el index
    formTareasPendientes = CursosYTareas.objects.filter(estado="espera", usuario = usuario)
    formTareasProceso = CursosYTareas.objects.filter(estado="proceso", usuario = usuario)
    formTareasTerminadas = CursosYTareas.objects.filter(estado="terminada", usuario = usuario)
    
    #proceso que obtiene los nombres de los cursos de tareas terminadas sin repetir
    formTareasTerminadas2 = set(formTareasTerminadas.values_list('curso', flat=True))

    #información que se cargará en el index
    data={
        'formTareasPendientes':formTareasPendientes,
        'formTareasProceso':formTareasProceso,
        'formTareasTerminadas':formTareasTerminadas,
        'formAnotaciones': formAnotaciones(),
        'formTareasTerminadasCursos':formTareasTerminadas2,
        'mensajes':cargarNotificaciones(request, 1),
        'mensajesSinLeer':cargarNotificaciones(request, 2),
        'fecha':datetime.date.today()
    }
    final = time.time()
    print("tiempo de ejecución:  ", final-inicio)
    return render(request, 'index/index.html', data)

def registro(request):
    error= False
    if request.method =='POST':
        formulario = UserRegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
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
        'cursosVerificados': EstadoDelCurso.objects.filter(verificacion='verificado'),
        'mensajes':cargarNotificaciones(request, 1),
        'mensajesSinLeer':cargarNotificaciones(request, 2)
    }
    #cursos= EstadoDelCurso()
    #return HttpResponse(cursos)
    return render(request, 'index/AgregarCurso.html', data, )



@login_required
def editarTarea(request, id):
    usuario = request.user.username
    formInfo = CursosYTareas.objects.get(pk = id)
    # for prim in formInfo:
    #     print(prim)
    print(formInfo.valor)
    if usuario == formInfo.usuario:
        data={
            'form':formAgregarCurso(instance=formInfo),
            'cursosVerificados': EstadoDelCurso.objects.filter(verificacion='verificado'),
            'id':id,
            'mensajes':cargarNotificaciones(request, 1),
            'mensajesSinLeer':cargarNotificaciones(request, 2)
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
    inicio = time.time()
    usuario = request.user.username
    cursosTerminados = CursosYTareas.objects.filter(usuario=usuario, estado='terminada').values_list('curso',flat=True)
    # configuracion = list(Settings.objects.get(usuario = usuario).dashboardActivos.split(","))

    configuracionOpen, created = Settings.objects.get_or_create(usuario=usuario,
    defaults={'usuario':usuario}
    )
    configuracion = list(configuracionOpen.dashboardActivos.split(","))
    print(configuracion)
        
    for config in configuracion:
        if config not in cursosTerminados:
            configuracion.remove(config)
    data={
        'cursosDisponibles':configuracion,
        'todosLosCursos':set(cursosTerminados),
        'mensajes':cargarNotificaciones(request, 1),
        'mensajesSinLeer':cargarNotificaciones(request, 2)
    }
    final = time.time()
    print("tiempo:  ", final-inicio)
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

def foo(request):
    mensaje = Mensajes.objects.get(pk=request.POST['id'])
    mensaje.leido=True
    mensaje.save()
    return HttpResponse("ok")

def cargarNotificaciones(request, opc):
    if opc==1:
        retornar = Mensajes.objects.filter(para=request.user.username).order_by('fecha')[::-1]
    else:
        retornar = Mensajes.objects.filter(para=request.user.username, leido=False)

    return retornar

def reportarBug(request):
    data={
        'mensajes':cargarNotificaciones(request, 1),
        'mensajesSinLeer':cargarNotificaciones(request, 2),
        'form':formReporte()
    }
    return render(request, 'index/reportarError.html', data)

@login_required
def enviarReporte(request):
    retornar ="invalido"
    if request.method =='POST':
        formDatos = formReporte(data=request.POST, files=request.FILES)
        if formDatos.is_valid():
            asunto = formDatos.cleaned_data['asunto']
            contenido = render_to_string('index/mensaje_correo.html',{
                'usuario':request.user.username,
                'asunto':asunto,
                'contenido':formDatos.cleaned_data['problema']
            })
            email = EmailMessage(
                asunto,
                contenido,
                settings.EMAIL_HOST_USER,
                ['melishamta2@gmail.com']
            )
            email.fail_silently = False
            try:
                img = formDatos.cleaned_data['imagen']
                email.attach(img.name, img.read(), img.content_type)
            except:
                pass
            email.send()

            notificacion = Mensajes()
            notificacion.para = request.user.username
            notificacion.de = "Sistema"
            notificacion.asunto = "El reporte ha sido enviado con éxito"
            notificacion.contenido="El reporte: {0} ha sido enviado, un administrador le responderá por este medio \
                una vez que el problema haya sido solucionado. \n Tu mensaje: {1}"\
                .format(formDatos.cleaned_data['asunto'],formDatos.cleaned_data['problema'])
            notificacion.save()
    

    return redirect(to=inicio)

        

