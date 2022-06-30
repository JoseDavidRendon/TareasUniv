
function crearLinea (id, mostrar){
    const datos = JSON.parse(mostrar);
    // console.log(datos);
    var labelss=Object.keys(datos);
    var dataForDatasets = [];
    for (var i = 0; i<Object.values(datos).length;i++){
        dataForDatasets=dataForDatasets.concat(Object.values(datos)[i]["calificacion"]);
    }
    console.log(dataForDatasets);
    // console.log(dataForDatasets);
    // for (var agg in labelss){
    //     console.log(datos[agg])
    // };
    // var largoDict = len(datos);
    // for (var i=1; i<5;i++){
    //     labelss+=i;
    // }
    // console.log(datos);
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
            }]
        },
            options: {
            scales: {
                y: {
                beginAtZero: true
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