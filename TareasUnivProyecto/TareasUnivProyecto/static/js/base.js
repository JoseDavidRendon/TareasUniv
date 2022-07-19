function ButtonsLoaded(){
    var elementos = document.getElementsByClassName('noclic')
    setTimeout(() => { 
        for (var i = 0; i<elementos.length; i++){
            elementos[i].classList.add('clicable')
        }    
     }, 500);
    
}
function expandirMensaje(id, idIcon){
    var elemento =document.getElementById(id);
    if (elemento.classList.contains('mensaje-abierto')){
        elemento.classList.remove('mensaje-abierto')    
        elemento.style.height='55px';
        elemento.classList.add('cerrado')
    } else {
        elemento.style.height='auto';
        elemento.classList.add('mensaje-abierto')
        elemento.classList.remove('cerrado')
    }
    var hijos = document.getElementById('mensaje-'+idIcon);
    console.log(hijos)
    if (hijos.contains(document.getElementById('mensaje-icon-'+idIcon))){
        console.log('existe')
        document.getElementById('mensaje-icon-'+idIcon).remove()
        $.ajax({
            type: "POST",
            url: "/foo",
            data: {"id":idIcon},
            headers: { "X-CSRFToken": getCookie("csrftoken")}
        });
        cantidadDeMensajes = document.getElementById('cantidad-de-mensajes').textContent;
        if (cantidadDeMensajes>1){
            document.getElementById('cantidad-de-mensajes').textContent = cantidadDeMensajes-1;
        } else {
            document.getElementById('indicador-mensajes').remove();
        }
        
    } else {
        console.log('Obvio no existe')
    }
    
}
function expandirContenedorMensajes(){
    var elemento = document.getElementById('contenedor-mensajes');
    if (elemento.classList.contains('contenedor-cerrado')){
        elemento.style.display='block'
        elemento.classList.add('expandir-contenedor-mensajes')
        elemento.classList.remove('contenedor-cerrado')
        elemento.classList.remove('minimizar-contenedor-mensajes')
    } else {
        elemento.classList.remove('expandir-contenedor-mensajes')
        elemento.classList.add('minimizar-contenedor-mensajes')
        setTimeout(() => { 
            elemento.style.display='none'
            elemento.classList.add('contenedor-cerrado')
        }, 150);
    }
    
}
function getCookie(c_name)
{
    if (document.cookie.length > 0)
    {
        c_start = document.cookie.indexOf(c_name + "=");
        if (c_start != -1)
        {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if (c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
 }

function expandirMenuUsuario(){
    document.getElementById('contenedor-usuario-menu').classList.add('mostrarDropdown')
}