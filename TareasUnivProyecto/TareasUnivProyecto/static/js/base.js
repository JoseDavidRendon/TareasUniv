function ButtonsLoaded(){
    var elementos = document.getElementsByClassName('noclic')
    setTimeout(() => { 
        for (var i = 0; i<elementos.length; i++){
            elementos[i].classList.add('clicable')
        }    
     }, 500);
    
}