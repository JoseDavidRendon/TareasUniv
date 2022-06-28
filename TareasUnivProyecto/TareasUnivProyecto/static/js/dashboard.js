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
    var ctx = document.getElementById('grafica-'+id).getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
        label: '# of Votes',
        data: [12, 19, 3, 5, 2, 3],
        borderColor:'rgba(255, 99, 132, 1)',
        borderWidth: 1
        }]
        },
        options: {
        scales: {
        y: {
        beginAtZero: true
        }
        }
        }
        });
}