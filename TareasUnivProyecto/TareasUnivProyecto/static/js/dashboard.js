
function crearLinea (id, mostrar){
    const labels = (tooltipItems) => {
            return " calificación: "+tooltipItems.raw+"%";
      };
    const datos = JSON.parse(mostrar);
    var labelss=Object.keys(datos);
    var dataForDatasets = [];
    for (var i = 0; i<Object.values(datos).length;i++){
        dataForDatasets=dataForDatasets.concat(Object.values(datos)[i]["calificacion"]);
    }
    var ctx = document.getElementById('grafica-'+id).getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'line',
    data: {
            // labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
            labels:labelss,
            
            datasets: [{
                label: 'Calificación',
                data: dataForDatasets,
                borderColor:'rgb(121, 180, 183)',
                borderWidth: 1,
                backgroundColor:'rgb(121, 180, 183)' ,
                pointRadius:7
            }]
        },
            options: {
            scales: {
                y: {
                beginAtZero: true,
                ticks: {
                    callback: function(value){
                        return value+"%";
                    }
                }
                }
            },
            plugins:{
                    legend:{
                        display:false
                    },
                    title: {
                        display: true,
                        text: 'Tareas',
                        fullSize:false
                    },
                    tooltip:{
                        callbacks: {
                            label: labels,
                    }
                }
            }
        }
    });
}
function crearDonut (id, valores){
    var ArrayValores = valores.split(",")
    var positivoPorcentaje = Math.round((ArrayValores[0]*100)/500);
    var negativoPorcentaje = Math.round((ArrayValores[1]*100)/500);
    var pendientePorcentaje = Math.round((ArrayValores[2]*100)/500);
    var porcentajeRestante = Math.round(100-(positivoPorcentaje+negativoPorcentaje+pendientePorcentaje))
    // ArraValores[0]=positivo, ArrayValores[1]=negativo, ArrayValores[2]=pendiente
    document.getElementById('texto-circular-verde-'+id).textContent=positivoPorcentaje+"%";
    document.getElementById('texto-circular-rojo-'+id).textContent=negativoPorcentaje+"%";
    document.getElementById('texto-circular-amarillo-'+id).textContent=pendientePorcentaje+"%";
var data={
    labels:[
        'Positivo',
        'Negativo',
        'Pendiente'
    ],
    datasets: [{
        label:"prueba",
        data:[positivoPorcentaje, negativoPorcentaje,pendientePorcentaje, porcentajeRestante],
        backgroundColor:[
            'rgba(167,209,111,1)',
            'rgb(241, 94, 94)',
            'rgb(232, 241, 94)',
            'rgb(225, 225, 225)'
        ],
        borderWidth:0
    }]
};
const labels = (tooltipItems) => {
    if(tooltipItems.label==""){
        return " Calificacion no asignada : "+tooltipItems.raw+"%";
    }else{
        var mostrar = " "+tooltipItems.label+" : "+tooltipItems.raw+"%";
        return mostrar;
    }
  };
var config ={
    type:'doughnut',
    data,
    options:{
        rotation:(180),
        scales:{
        },
        plugins:{
            legend:{
                display:false,
                
            },
            title: {
                display: true,
                text: 'Calificaciones',
                fullSize:false
            },
            tooltip:{
                callbacks: {
                    label: labels,
            }
        }
    }
}
};

var myChart = new Chart(
    document.getElementById('grafica-circular-'+id), config
)

}



function crearDonutProgreso (id, progreso){
    var progresoPorcentaje = ((progreso*100)/500)
    document.getElementById('texto-circular-'+id).textContent=Math.round(progresoPorcentaje)+"%";
    var percent = 100-progresoPorcentaje;
    var data={
        labels:[
            'Completado',
        ],
        datasets: [{
            label:"prueba",
            data:[progresoPorcentaje, percent],
            backgroundColor:[
                'rgb(121, 180, 183)',
                'rgb(225, 225, 225)'
            ],
            borderWidth:0
        }]
    };
    const labels = (tooltipItems) => {
        if(tooltipItems.label==""){
            return " Calificacion no asignada : "+tooltipItems.raw+"%";
        }else{
            var mostrar = " "+tooltipItems.label+" : "+tooltipItems.raw+"%";
            return mostrar;
        }
      };
    var config ={
        type:'doughnut',
        data,
        options:{
            rotation:(180),
            scales:{
            },
            plugins:{
                legend:{
                    display:false,
                    
                },
                
            title: {
                display: true,
                text: 'Progreso',
                fullSize:false
            },
                tooltip:{
                    callbacks: {
                        label: labels,
                }
            }
        }
    }
    };
    
    var myChart = new Chart(
        document.getElementById('grafica-circular2-'+id), config
    );
}

function comprobarChecked(id, comprobado){
    
    if (comprobado ==1){
        var checkboxContainer = document.getElementById(id);
        document.getElementById('checkbox-'+id).checked=true;
        checkboxContainer.classList.add('checkedContainer');
    }
}
function buscadorDeCursos(){
    var casilla = document.getElementsByClassName('casilla-curso');
    var inputText = document.getElementById('busqueda-de-cursos');
    for (var i = 0; i< casilla.length;i++){
        var idd = casilla[i].innerHTML;
        document.getElementById(idd).style.display="none";
        if (casilla[i].innerHTML.includes(inputText.value.toLowerCase())){
            document.getElementById(idd).style.display="flex";
        }
    }
}
function selectAll(state){
    if (state){
        var coleccion = document.getElementsByClassName('checkboxAll');
        for (var i =0;i<coleccion.length;i++){
                coleccion[i].checked=true;
                id = coleccion[i].getAttribute('name');
                var checkboxContainer = document.getElementById(id);
                checkboxContainer.classList.add('checkedContainer');
        }
    }else{
        var coleccion = document.getElementsByClassName('checkboxAll');
        for (var i =0;i<coleccion.length;i++){
                coleccion[i].checked=false;
                id = coleccion[i].getAttribute('name');
                var checkboxContainer = document.getElementById(id);
                checkboxContainer.classList.remove('checkedContainer');
        }
    }
}
function clickCheckbox(id){
    var checkboxElement = document.getElementById('checkbox-'+id);
    var checkboxContainer = document.getElementById(id);
    if (checkboxElement.checked){
        checkboxElement.checked=false;
        checkboxContainer.classList.remove('checkedContainer');
    } else {
        checkboxElement.checked=true;
        checkboxContainer.classList.add('checkedContainer');

    }

}
function crearBarraPromedio(id, originDict){
    var diccionario = originDict.replaceAll('&#x27;',"\"");
    var correctedDiccionario = JSON.parse(diccionario);
    var marcador = document.getElementById('marcador-'+id);
    var marcadorGlobal = document.getElementById('marcador-global-'+id);
    marcador.style.left=correctedDiccionario['promedioPersonal']+"%";
    marcadorGlobal.style.left=correctedDiccionario['promedioGlobal']+"%";
    if (correctedDiccionario['promedioPersonal']  > 80){
        document.getElementById('mensaje-top-'+id).style.right="100px"
    }
    if (correctedDiccionario['promedioGlobal']  > 80){
        document.getElementById('mensaje-bot-'+id).style.right="100px"
    }
    if (correctedDiccionario['promedioPersonal']  < 20){
        document.getElementById('mensaje-top-'+id).style.left="0px"
    }
    if (correctedDiccionario['promedioGlobal']  < 20){
        document.getElementById('mensaje-bot-'+id).style.left="0px"
    }
    document.getElementById('porcentaje-top-'+id).textContent=correctedDiccionario['promedioPersonal']+"%";  
    document.getElementById('porcentaje-bot-'+id).textContent=correctedDiccionario['promedioGlobal']+"%";  
    document.getElementById('calificacion-definitiva-'+id).textContent=correctedDiccionario['calificacion'];
    if(correctedDiccionario['calificacion'] <3.0){
        document.getElementById('calificacion-definitiva-'+id).style.color="red"
    } else if (correctedDiccionario['calificacion'] <3.6){
        document.getElementById('calificacion-definitiva-'+id).style.color="yellow"
    } else{
        document.getElementById('calificacion-definitiva-'+id).style.color="green"
    }
    if(correctedDiccionario['error']){
        document.getElementById('conjunto-de-graficas-'+id).style.filter="blur(6px)";
        document.getElementById('contenedor-graficaLineal-'+id).style.filter="blur(6px)";
        document.getElementById('contenedor-barra-padre-'+id).style.filter="blur(6px)";
        document.getElementById('contenedor-graficas-'+id).style.filter="saturate(13%)";
        document.getElementById('error-curso-'+id).style.display="block";
        document.getElementById('icon-warning-'+id).style.display="flex"
    }
}