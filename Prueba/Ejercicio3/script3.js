const tamano = 5;
let vector1= [];
let vector2 = [];
console.log ('--ingresa el primer vector--');

for (let i = 0; i < tamano ; i++){

let nuevoNumero = parseInt(prompt(`Vector 1 - Ingresa el Numero ${i+1} de ${tamano}:`));

if (vector1.length ===0 || nuevoNumero>= Math.max(...vector1)){

    vector1.push(nuevoNumero);

}

else {
    alert ("Error: Debes ingresar un numero mayor o igual al anterior. Intentalo de nuevo");

    i--;
}
}
console.log("El segundo vector ordenado es:", vector1 );

for (let i = 0;i<tamano;i++){

let nuevoNumero2 = parseInt(prompt(`Vector 2 - Ingresa el Numero ${i+1} de ${tamano}:`));

if (vector2.length ===0 || nuevoNumero2>= Math.max(...vector2)){

    vector2.push(nuevoNumero2);

}

else {
    alert ("Error: Debes ingresar un numero mayor o igual al anterior. Intentalo de nuevo");

    i--;
}
}

console.log("El segundo vector ordenado es:", vector2 );

const listaFinal = vector1.concat(vector2).sort((a, b)=> a - b);

console.log("La lista final ordenada es:", listaFinal);
alert ("La lista final es:" + listaFinal.join(", "));