from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators  import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm


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
            error=True
    data={
        'form':UserRegisterForm(),
        'error':error
        }       
    return render(request, 'registration/registro.html', data)

def salir(request):
    logout()
    return redirect(to="/")
