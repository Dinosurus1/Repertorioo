const edades = [];
//Almacenar las edades con validacion
for (let i = 0; i < 10; i++){
    let edad;
    do {
       edad = parseInt(prompt (`Ingresa la edad de la persona ${i + 1}:`));
        if (isNaN(edad) || edad < 1 || edad > 120) {
            alert("Error: Ingresa una edad valida entre 1 y 120 años.");

       }

    } while (isNaN(edad) || edad < 1 || edad > 120); 
    edades.push(edad);
}

//Inicializar contadores y calcular estadisticas
let menoresEdad= 0;
let mayoresEdad= 0;
let adultosMayores= 0;


for (const edad of edades) {
    if (edad<18){
        menoresEdad++;
    }
    if (edad>18){
        mayoresEdad++;
    }
    if (edad>60){
        adultosMayores++;
    }

}
    

    const edadMasBaja = Math.min(...edades);
    const edadMasAlta = Math.max(...edades);

    const sumaEdades = edades.reduce((acumulador, edadActual)=> acumulador + edadActual, 0);
    const promedioEdades = sumaEdades / edades.length;
//mostras resultados
    const resultados = `
--- Resultados del Análisis de Edades ---
Cantidad de menores de edad: ${menoresEdad}
Cantidad de mayores de edad: ${mayoresEdad}
Cantidad de adultos mayores: ${adultosMayores}
------------------------------------
Edad más baja: ${edadMasBaja}
Edad más alta: ${edadMasAlta}
Promedio de edades: ${promedioEdades.toFixed(2)}
`;

alert(resultados);