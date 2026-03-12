//                              Ejercicio de Evaluación: Pilas (Stacks)

//  Enunciado:
//      1. Crea una pila vacía.
//      2. Apila los elementos 4, 5, 6.
//      3. Desapila un elemento y guárdalo en una variable.
//      4. Obtén el elemento de arriba sin retirarlo y guárdalo en una variable.
//      5. Comprueba si la pila está vacía.



// Resolver Acá:

// 1. Crear pila vacía
let stack = [];

console.log(stack)

// 2. Apilar 4, 5, 6
stack.push(4);
stack.push(5);
stack.push(6);
console.log(stack);

// 3. Desapilar un elemento y guardarlo en una variable
const Elem_Remove = stack.pop();

console.log(Elem_Remove);
console.log(stack);
// 4. Obtener el elemento de arriba sin retirarlo y guardarlo en una variable
const peek = stack[stack.length - 1];
console.log(peek);
// 5. Comprobar si la pila está vacía

const empty = stack.length === 0;
console.log(empty)
// Resultado esperado:
//  - 1 = []
//  - 2 = [4,5,6]
//  - 3 = elementoEliminado = 6, stack = [4,5]
//  - 4 = peek = 5
//  - 5 = false