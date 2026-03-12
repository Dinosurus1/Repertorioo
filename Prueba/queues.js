
// Enunciado:
//  1. Crea una cola vacía.
//  2. Encola "usuarioA", "usuarioB", "usuarioC".
//  3. Desencola un elemento y guárdalo en una variable.
//  4. Obtén el elemento al frente sin retirarlo y guárdalo en una variable.
//  5. Comprueba si la cola está vacía.



// Resolver Acá:

// 1. Crear cola vacía
let queue =[];
console.log (queue);
// 2. Encolar "usuarioA", "usuarioB", "usuarioC"
queue.push('UsuarioA');
queue.push('UsuarioB');
queue.push('UsuarioC');
console.log(queue);
// 3. Desencolar un elemento y guardarlo en una variable
const guardad_elemento = queue.shift();
console.log(queue);


// 4. Obtener el frente sin retirarlo y guardarlo en una variable
const front = queue[0];
console.log(front)

// 5. Comprobar si la cola está vacía

const empty = queue.length === 0
console.log(empty)

// Resultado esperado:
//  - 1 = []
//  - 2 = ["usuarioA","usuarioB","usuarioC"]
//  - 3 = usuarioA eliminado, queue = ["usuarioB","usuarioC"]
//  - 4 = "usuarioB"
//  - 5 = false