from pyexpat.errors import messages
from xml.dom import ValidationErr
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators  import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm, formAgregarCurso
from .models import CursosYTareas
# Create your views here.

@login_required
def inicio(request):
    
    
    return render(request, 'index/index.html')

def registro(request):
    error= False
    if request.method =='POST':
        formulario = UserRegisterForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Profile details updated.')
            return redirect(to="/")
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
    return redirect(to="/")

def agregarCurso(request):
    if request.method == 'POST':
        formulario = formAgregarCurso(request.POST)
        if formulario.is_valid():
            form=CursosYTareas()
            form.curso = formulario.cleaned_data['curso']
            form.estado = formulario.cleaned_data['estado']
            form.tarea = formulario.cleaned_data['tarea']
            form.valor = formulario.cleaned_data['valor']
            form.save()
            data={
                'form':formAgregarCurso(),
                'error':False,
            }
            return render(request, 'index/AgregarCurso.html', data)
        else:
            data={
                'form':formAgregarCurso(),
                'error':True,
            }
            return render(request, 'index/AgregarCurso.html', data)

def nuevoCurso(request):
    data={
        'form':formAgregarCurso()
        
    }
    return render(request, 'index/AgregarCurso.html', data, )