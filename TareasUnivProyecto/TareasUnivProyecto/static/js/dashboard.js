
function crearLinea (id){
    var ctx = document.getElementById('grafica-'+id).getContext('2d');
    var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange'],
        datasets: [{
        label: 'Calificación',
        data: [12, 19, 3, 5, 2, 3],
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
function crearDonut (id){

var data={
    labels:[
        '50%',
        '50%',
        '50%'
    ],
    datasets: [{
        label:"prueba",
        data:[50, 30,10,20],
        backgroundColor:[
            'rgba(167,209,111,1)',
            'rgb(232, 241, 94)',
            'rgb(241, 94, 94)',
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
    console.log("Porcentaje: "+progresoPorcentaje+" original: "+progreso);
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