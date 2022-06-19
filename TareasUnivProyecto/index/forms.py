from dataclasses import fields
import datetime
from tkinter import Widget
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CursosYTareas

class UserRegisterForm(UserCreationForm):
    username = forms.CharField()
    email = forms.EmailField()
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)
     
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:" ff" for k in fields}

#class formAgregarCurso(forms.Form):
    
#    curso = forms.CharField( max_length=100)
#    tarea = forms.CharField( max_length=100)
#    valor = forms.IntegerField( max_value=500)
#    estado = forms.CharField()
#    entrega = forms.DateField(widget=forms.SelectDateWidget())

class formAgregarCurso(forms.ModelForm):
    

    class Meta:
        model = CursosYTareas
        fields=['curso', 'tarea', 'valor', 'estado', 'entrega', 'anotacion']
        widgets = {
            'entrega':forms.SelectDateWidget(),
        }
    def __init__(self, *args, **kwargs):
        super(self.__class__, self).__init__(*args, **kwargs)
        
        self.fields['anotacion'].required = False
        


class formAnotaciones(forms.Form):
    anotacion = forms.CharField(widget=forms.Textarea)
