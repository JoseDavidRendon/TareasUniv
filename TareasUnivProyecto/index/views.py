from pyexpat.errors import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators  import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.

@login_required
def inicio(request):
    return render(request, 'index/index.html')

def registro(request):
    data={
        'form':CustomUserCreationForm()
        }
    if request.method =='POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user=authenticate(username=formulario.cleaned_data['username'], password=formulario.cleaned_data['password1'])
            login(request, user)
            messages.success(request, 'Profile details updated.')
            return redirect(to="/")
            
    return render(request, 'registration/registro.html', data)

def salir(request):
    logout()
    return redirect(to="/")