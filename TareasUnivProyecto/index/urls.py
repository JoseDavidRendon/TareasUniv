from django.urls import path
from index.views import inicio, registro, salir, agregarCurso, nuevoCurso

urlpatterns = [
    path('', inicio, name="inicio"),
    path('registrarse/', registro, name="registro"),
    path('salir/', salir, name='logout'),
    path('agregarCurso/', agregarCurso, name="agregarCurso"),
    path('agregarTarea/', nuevoCurso, name="agregarTarea"),
]
 