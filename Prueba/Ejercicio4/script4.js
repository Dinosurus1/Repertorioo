// Array principal para guardar a todas las personas encuestadas
const personasEncuestadas = [];
const numeroDeEncuestas = 6; // Límite de personas a encuestar

// --- FUNCIÓN PARA AGREGAR UNA PERSONA ---
function agregarPersona() {
    // Verificamos si ya alcanzamos el límite
    if (personasEncuestadas.length >= numeroDeEncuestas) {
        alert(`Ya se ha alcanzado el límite de ${numeroDeEncuestas} personas encuestadas.`);
        return; // Salimos de la función si ya estamos llenos
    }

    alert(`--- Ingresando Persona ${personasEncuestadas.length + 1} de ${numeroDeEncuestas} ---`);

    // 1. Creamos un objeto vacío para la nueva persona
    const nuevaPersona = {};

    // 2. Pedimos los datos personales y los guardamos en el objeto
    nuevaPersona.nombre = prompt("Nombre completo:");
    nuevaPersona.identificacion = prompt("Número de identificación (cédula):");
    nuevaPersona.fechaNacimiento = prompt("Fecha de nacimiento (DD/MM/AAAA):");
    nuevaPersona.correo = prompt("Correo electrónico:");
    nuevaPersona.ciudadResidencia = prompt("Ciudad de residencia:");
    nuevaPersona.ciudadOrigen = prompt("Ciudad de origen:");

    // 3. Creamos un array vacío para las canciones dentro del objeto persona
    nuevaPersona.cancionesFavoritas = [];

    // 4. Pedimos las 3 canciones favoritas
    for (let i = 0; i < 3; i++) {
        alert(`--- Canción Favorita ${i + 1} de 3 ---`);
        const cancion = {}; // Objeto para cada canción
        cancion.artista = prompt("Artista:");
        cancion.titulo = prompt("Título de la canción:");
        nuevaPersona.cancionesFavoritas.push(cancion);
    }

    // 5. Agregamos el objeto persona completo al array principal
    personasEncuestadas.push(nuevaPersona);
    alert(`¡Persona "${nuevaPersona.nombre}" agregada con éxito!`);
}

// --- FUNCIÓN PARA MOSTRAR UNA PERSONA ---
function mostrarPersona() {
    if (personasEncuestadas.length === 0) {
        alert("Aún no se ha agregado ninguna persona.");
        return;
    }

    // Pedimos la posición (índice) que el usuario quiere ver
    const posicion = parseInt(prompt(`Ingresa la posición de la persona que deseas ver (de 1 a ${personasEncuestadas.length}):`));

    // Validamos que la posición sea un número válido y esté dentro del rango
    if (isNaN(posicion) || posicion < 1 || posicion > personasEncuestadas.length) {
        alert("Posición no válida. Por favor, ingresa un número correcto.");
        return;
    }

    // El usuario ingresa 1, pero en el array la posición es 0
    const indice = posicion - 1; 
    const personaSeleccionada = personasEncuestadas[indice];

    // Preparamos el texto para mostrar las canciones
    let infoCanciones = "";
    personaSeleccionada.cancionesFavoritas.forEach((cancion, i) => {
        infoCanciones += `\n  Canción ${i + 1}: "${cancion.titulo}" de ${cancion.artista}`;
    });

    // Mostramos toda la información en una alerta
    alert(`--- Información de la Persona #${posicion} ---
        \nNombre: ${personaSeleccionada.nombre}
        \nIdentificación: ${personaSeleccionada.identificacion}
        \nFecha de Nacimiento: ${personaSeleccionada.fechaNacimiento}
        \nCorreo: ${personaSeleccionada.correo}
        \nCiudad de Residencia: ${personaSeleccionada.ciudadResidencia}
        \nCiudad de Origen: ${personaSeleccionada.ciudadOrigen}
        \n--- Canciones Favoritas ---${infoCanciones}
    `);
}


// --- MENÚ PRINCIPAL ---
let opcion = "";
while (opcion !== "c") {
    opcion = prompt(`--- MENÚ EMISORA ---
        Personas registradas: ${personasEncuestadas.length} de ${numeroDeEncuestas}

        a. Agregar una persona
        b. Mostrar información de una persona
        c. Salir

        Ingresa tu opción:
    `);

    // Convertimos a minúscula para evitar errores
    opcion = opcion ? opcion.toLowerCase() : ""; 

    switch (opcion) {
        case "a":
            agregarPersona();
            break;
        case "b":
            mostrarPersona();
            break;
        case "c":
            alert("¡Gracias por usar el programa!");
            break;
        default:
            if (opcion !== "c") {
                alert("Opción no válida. Por favor, elige 'a', 'b' o 'c'.");
            }
            break;
    }
}