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
    var porcentajeArregladoRojo = porcentajeRojo-porcentajeVerde;
    var porcentajeArregladoAmarillo = porcentajeAmarillo-porcentajeRojo;
    document.getElementById('numero-mostrar-calificaciones-verde-'+id).textContent=porcentajeVerde;
    document.getElementById('numero-mostrar-calificaciones-amarillo-'+id).textContent=porcentajeArregladoAmarillo;
    document.getElementById('numero-mostrar-calificaciones-rojo-'+id).textContent=porcentajeArregladoRojo;
    document.getElementById('barra-mostrar-verde-'+id).style.transform='rotate('+numRotarVerde+'deg)';
    document.getElementById('barra-mostrar-amarillo-'+id).style.transform='rotate('+numRotarAmarillo+'deg)';
    document.getElementById('barra-mostrar-rojo-'+id).style.transform='rotate('+numRotarRojo+'deg)';
}

function crearLinea (id){
    new Morris.Line({
        // ID of the element in which to draw the chart.
        element: id,
        // Chart data records -- each entry in this array corresponds to a point on
        // the chart.
        data: [
            { year: '2008', value: 20 },
            { year: '2009', value: 10 },
            { year: '2010', value: 5 },
            { year: '2011', value: 5 },
            { year: '2012', value: 20 }
        ],
        // The name of the data record attribute that contains x-values.
        xkey: 'year',
        // A list of names of data record attributes that contain y-values.
        ykeys: ['value'],
        // Labels for the ykeys -- will be displayed when you hover over the
        // chart.
        labels: ['Value'],
        resize: true,
        });
}