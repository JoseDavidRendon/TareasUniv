from django.urls import include, path
from index.views import inicio, registro, salir, agregarCurso, nuevoCurso, editarTarea, actualizarCurso, borrarCurso, actualizarAnotacion, dashboard, editarCalificado, actualizarConfigDashboard, foo, reportarBug,enviarReporte




urlpatterns = [
    path('', inicio, name="inicio", ),
    path('registrarse/', registro, name="registro"),
    path('salir/', salir, name='logout'),
    path('agregarCurso/', agregarCurso, name="agregarCurso"),
    path('agregarTarea/', nuevoCurso, name="agregarTarea"),
    path('editarTarea/<id>/', editarTarea, name="editarTarea"),
    path('actualizarCurso/', actualizarCurso, name="actualizarCurso"),
    path('borrarCurso/<id>/', borrarCurso, name="borrarCurso"),
    path('borrarCurso/<id>/', borrarCurso, name="borrarCurso"),
    path('actualizarAnotacion/', actualizarAnotacion, name='actualizarAnotacion'),
    path('dashboard/', dashboard, name='dashboard'),
    path('editarCalificado/', editarCalificado, name='editarCalificado'),
    path('actualizarConfigDashboard/', actualizarConfigDashboard, name='actualizarConfigDashboard'),
    path('foo', foo, name='foo'),
    path('reportarBug', reportarBug ,name='reportarBug'),
    path('enviarReporte',enviarReporte,name='enviarReporte')
]
 
 