/*$( document ).ready(function() {
    // Handler for .ready() called.
    alert('Todo bien');
  });*/


function eliminarEquipo(id) {
  document.getElementById("id_equipo_eliminar").value = id;
}

function eliminarArea(id) {
  document.getElementById("id_area_eliminar").value = id;
}

function marcarBajado(id) {
  document.getElementById("id_trabajo_materiales").value = id;
}

function editarEquipo(id, nombre, telefono, direccion,nit) {
  
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("nombre_editar").value = nombre;
  document.getElementById("telefono_editar").value = telefono;
  document.getElementById("direccion_editar").value = direccion;
  document.getElementById("nit_editar").value = nit;
}

function editarProduct(id, nombre, descripcion,  categoria,cantidad, precio) {
  document.getElementById("id_producto_editar").value = id;
  document.getElementById("nombre_editar").value = nombre;
  document.getElementById("descripcion_editar").value = descripcion;
  document.getElementById("categoria_editar").value = categoria;
  document.getElementById("cantidad_editar").value = cantidad;
  document.getElementById("precio_editar").value = precio;
}

function historialPreventivo(id,solicitadoh,supervisado,responsable, subtotalpiezas, subtotalmo, fecha) {
  
  document.getElementById("hist_preventivo_editar").value = id;
  document.getElementById("hist_solicitadoh").value = solicitadoh;
  document.getElementById("hist_supervisadoh").value = supervisado;
  document.getElementById("hist_responsable").value = responsable;
  document.getElementById("hist_subtotalpiezas").value = subtotalpiezas;
  document.getElementById("hist_subtotalmo").value = subtotalmo;
  document.getElementById("hist_fecha_programada_editar").value = fecha;
}

function editarPreventivo(id, fecha, contacto, piezas, actividades, comentarios, total) {
  
  document.getElementById("id_preventivo_editar").value = id;
  document.getElementById("fecha_editar").value = fecha;
  document.getElementById("contacto_editar").value = contacto;
  document.getElementById("actividades_editar").value = actividades;
  document.getElementById("comentarios_editar").value = comentarios;
  document.getElementById("piezas_editar").value = piezas;
  document.getElementById("total_editar").value = total;
}

function editarCorrectivo(id, nombre, telefono, direccion,nit) {
  
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("nombre_editar").value = nombre;
  document.getElementById("telefono_editar").value = telefono;
  document.getElementById("direccion_editar").value = direccion;
  document.getElementById("nit_editar").value = nit;
}

function eliminarCorrectivo(id) {
  document.getElementById("id_correctivo_eliminar").value = id;
}

function historialCorrectivo(id,solicitadoh,supervisado,responsable, subtotalpiezas, subtotalmo, fecha) {
  
  document.getElementById("hist_correctivo_editar").value = id;
  document.getElementById("hist_solicitadoh").value = solicitadoh;
  document.getElementById("hist_supervisadoh").value = supervisado;
  document.getElementById("hist_responsable").value = responsable;
  document.getElementById("hist_subtotalpiezas").value = subtotalpiezas;
  document.getElementById("hist_subtotalmo").value = subtotalmo;
  document.getElementById("hist_fecha_programada_editar").value = fecha;
}

function eliminarPreventivo(id) {
  document.getElementById("id_preventivo_eliminar").value = id;
}

function eliminarProducto(id) {
  document.getElementById("id_producto_eliminar").value = id;
}

function editarPersonal(id, nombre, telefono, cargo) {
  document.getElementById("id_personal_editar").value = id;
  document.getElementById("nombre_editar").value = nombre;
  document.getElementById("telefono_editar").value = telefono;
  document.getElementById("cargo_editar").value = cargo;
}

function eliminarPersonal(id) {
  document.getElementById("id_personal_eliminar").value = id;
}

function borrarContent(){
  document.getElementById("search").value = "";
}

function seleccionarCliente(id, nombre){
 document.getElementById("id_cliente").value = id;
 document.getElementById("cliente").value = nombre;
}

function activarEspera(){
  const btn = document.getElementById("btn");
  btn.innerHTML = 'Generando ... <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true"></span>';
  btn.disabled = true;
}

$(document).ready(function () {

  $('#myTable').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table2').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
  $('#table3').DataTable({
    "language": {
      "url": "../static/index/js/idiom.json"},
    "lengthMenu": [[10, 25, 50], [10, 25, 50]],
    dom: 'Bfrtip',
    buttons: [
      { extend: 'csv' },
      { extend: 'print'},
    ]
  });
});
 