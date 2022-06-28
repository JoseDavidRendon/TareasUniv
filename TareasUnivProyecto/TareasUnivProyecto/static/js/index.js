function clickBtnCalificado(id){
    document.getElementById('boton-edit-calif-'+id).style.display="none";
    var contenedor = document.getElementById('selector-'+id);
    if (contenedor.classList.contains('Checked')){
        desactivarCalificado(id);
        document.getElementById('check-ok-'+id).style.display="block";
        document.getElementById('insertar-nota-'+id).style.display="none";
    } else {
        activarCalificado(id);
        document.getElementById('insertar-nota-'+id).style.display="block";
        document.getElementById('check-ok-'+id).style.display="block";
        document.getElementById('insertar-nota-'+id).disabled=false;
    }
}
function activarCalificado(id){
    var contenedor = document.getElementById('selector-'+id);
    if (contenedor.classList.contains('NoChecked')){
        contenedor.classList.remove('NoChecked');
    }
    contenedor.classList.add('Checked');
    contenedor.style.backgroundColor="rgb(165, 244, 165)";
    document.getElementById('boton-interior-'+id).style.marginLeft="32px";
    document.getElementById('check-'+id).setAttribute("value", "1");
    
}
function desactivarCalificado(id){
    document.getElementById('insertar-nota-'+id).style.display="none"
    var contenedor = document.getElementById('selector-'+id);
    if (contenedor.classList.contains('Checked')){
        contenedor.classList.remove('Checked');
    }
    contenedor.classList.add('NoChecked');
    contenedor.style.backgroundColor="rgb(244, 165, 165)"
    document.getElementById('boton-interior-'+id).style.marginLeft="0px";
    document.getElementById('check-'+id).setAttribute("value", "0");
    
}
function defaultEditCalif(id){
    document.getElementById('boton-edit-calif-'+id).style.display="block";
}


function scriptBackground(name_id) {

    document.getElementById("pantalla-desenfoque-"+name_id).classList.add('desenfoque');

    document.getElementById("id-form-anotacion-"+name_id).style.display="none";

    document.getElementById("anotacion-actual-"+name_id).style.display="block";

    document.getElementById("reset-btn-"+name_id).click();    

    document.getElementById('expandir-'+name_id).classList.add('show');
}

function noScriptBackground(name_id) {

    document.getElementById("mensaje-"+name_id).click();

    document.getElementById("pantalla-desenfoque-"+name_id).classList.remove('desenfoque');

    document.getElementById("expandir-"+name_id).classList.remove("sobreponer");

    document.getElementById("anotacion-actual-"+name_id).style.display="none";

    document.getElementById('expandir-'+name_id).classList.remove('show');
}

function AbrirEditor(name_id) {
    
    document.getElementById("anotacion-actual-"+name_id).style.display="none";

    document.getElementById("id-form-anotacion-"+name_id).style.display="block";
}

function colapsarContenedorTarea(contenedor, titulo, icon){
    var elemento = document.getElementById(contenedor);
    var titulo_elemento = document.getElementById(titulo);
    var icon_titulo = document.getElementById(icon);

    if (elemento.classList.contains('colapsar-css')){
        
        elemento.classList.remove('colapsar-css')
        titulo_elemento.style.opacity="100%";
        icon_titulo.style.transform= 'rotate(180deg)';

    } else {

        elemento.classList.add('colapsar-css')
        titulo_elemento.style.opacity="50%";
        icon_titulo.style.transform= 'rotate(0deg)';

    }

}

function editarCalificacion(id){
    document.getElementById('check-ok-'+id).style.display="block";
    document.getElementById('boton-edit-calif-'+id).style.display="none";
    document.getElementById('insertar-nota-'+id).disabled=false;
}