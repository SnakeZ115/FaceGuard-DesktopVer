let fecha = document.getElementById('fecha');
let fechaActual = new Date();

// Formateamos la fecha en un formato legible
let options = { year: 'numeric', month: 'long', day: 'numeric' };
let fechaFormateada = fechaActual.toLocaleDateString('es-ES', options);

// Actualizamos el contenido del span con la fecha formateada
fecha.textContent = fechaFormateada;