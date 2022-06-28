function mostrarBarra(id, numero){
    var progreso = Math.trunc(100-(((500-numero)*100)/500));
    var numRotar = ((progreso)*180)/100;
    document.getElementById('numero-mostrar-'+id).textContent=progreso;
    document.getElementById('barra-mostrar-'+id).style.transform='rotate('+numRotar+'deg)'
}
function mostrarBarraCalificaciones(id, numeroVerde, numeroAmarillo, numeroRojo){
    var porcentajeVerde = Math.trunc(100-(((500-numeroVerde)*100)/500));
    var porcentajeAmarillo = Math.trunc(100-(((500-numeroAmarillo)*100)/500));
    var porcentajeRojo = Math.trunc(100-(((500-numeroRojo)*100)/500));
    var numRotarVerde = ((porcentajeVerde)*180)/100;
    var numRotarAmarillo = ((porcentajeAmarillo)*180)/100;
    var numRotarRojo = ((porcentajeRojo)*180)/100;
    document.getElementById('numero-mostrar-calificaciones-verde-'+id).textContent=porcentajeVerde;
    document.getElementById('barra-mostrar-verde-'+id).style.transform='rotate('+numRotarVerde+'deg)';
    document.getElementById('barra-mostrar-amarillo-'+id).style.transform='rotate('+numRotarAmarillo+'deg)';
    document.getElementById('barra-mostrar-rojo-'+id).style.transform='rotate('+numRotarRojo+'deg)';
}