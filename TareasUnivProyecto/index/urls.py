from django.urls import path
from index.views import inicio, registro, salir, agregarCurso, nuevoCurso, editarTarea, actualizarCurso, borrarCurso, \
    enviarAnotacion, actualizarAnotacion



urlpatterns = [
    path('', inicio, name="inicio"),
    path('registrarse/', registro, name="registro"),
    path('salir/', salir, name='logout'),
    path('agregarCurso/', agregarCurso, name="agregarCurso"),
    path('agregarTarea/', nuevoCurso, name="agregarTarea"),
    path('editarTarea/<id>/', editarTarea, name="editarTarea"),
    path('actualizarCurso/', actualizarCurso, name="actualizarCurso"),
    path('borrarCurso/<id>/', borrarCurso, name="borrarCurso"),
    path('borrarCurso/<id>/', borrarCurso, name="borrarCurso"),
    path('enviarAnotacion/', enviarAnotacion, name="enviarAnotacion"),
    path('actualizarAnotacion/', actualizarAnotacion, name="actualizarAnotacion"),

]
 
 