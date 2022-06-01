from django.urls import path
from index.views import inicio, registro, salir

urlpatterns = [
    path('', inicio),
    path('registrarse/', registro, name="registro"),
    path('salir/', salir, name='logout')
]
