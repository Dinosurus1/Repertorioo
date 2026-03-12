//              Ejercicio de Evaluación: Listas / Arrays

// Enunciado:
//  Dado un array de números [5, 15, 25]:
//      1. Agrega el número 35 al final.
//      2. Elimina el ultimo elemento y guárdalo en una variable.
//      3. Comprueba si el array contiene el valor 15.
//      4. Obtén la longitud final del array.



// Resolver Acá:


// 0. Crear el array

let numbers = [5, 15, 25]

// 1. Agregar el numero 35

numbers.push (35)
//console.log(numbers)

// 2. Eliminar el ultimo y guardar en una variable llamada 'last'
const last = numbers[3]
numbers.pop();
console.log (numbers)
console.log(last)
// 3. Verificar existencia de 15
console.log(numbers.includes(15))

// 4. Obtener longitud del arreglo en una variable llamada 'len'

console.log(numbers.length)


// Resultado esperado:
//  - 1 = [5, 15, 25, 35]
//  - 2 = 35, arr = [5,15, 25]
//  - 3 = true
//  - 4 = 3
