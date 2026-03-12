//                            Ejercicio de Evaluación: Listas Enlazadas

// Enunciado:
//  1. Crea una lista enlazada y añade: "M", "N", "O".
//  2. Elimina el nodo con valor "N".
//  3. Recorre e imprime los valores restantes.
//  4. Inserta un nuevo nodo con valor "Y" justo después de "M".
//  5. Elimina el nodo con valor "O".
//  6. Recorre e imprime los valores finales.



// Constructor de la clase Linked-List y Node, NO TOCAR
class Node {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
  }

  add(value) {
    const node = new Node(value);
    if (!this.head) {
      this.head = node;
    } else {
      let curr = this.head;
      while (curr.next) curr = curr.next;
      curr.next = node;
    }
  }

  remove(value) {
    if (!this.head) return;
    if (this.head.value === value) {
      this.head = this.head.next;
      return;
    }
    let curr = this.head;
    while (curr.next && curr.next.value !== value) curr = curr.next;
    if (curr.next) curr.next = curr.next.next;
  }

  insertAfter(target, value) {
    let curr = this.head;
    while (curr && curr.value !== target) curr = curr.next;
    if (curr) {
      const node = new Node(value);
      node.next = curr.next;
      curr.next = node;
    }
  }

  traverse() {
    let curr = this.head;
    while (curr) {
      console.log(curr.value);
      curr = curr.next;
    }
  }
}

// Resolver Acá:


// 1. Crear la lista y agregar los valores "M", "N", "O"

let lista= new LinkedList();
[lista.add("M"), lista.add('N'), lista.add('O')];
//console.log(lista)

// 2. Eliminar el nodo con valor "N"
console.log('-----------------------------------------')
lista.remove ('N')
//console.log(lista)
// 3. Recorre la lista e imprime los valores
//lista.traverse();

// 4. Insertar un nodo con valor "Y" después de "M"

lista.insertAfter('M', "Y")

//lista.traverse();

// 5. Eliminar el nodo con valor "O"

lista.remove ("O");
//console.log(lista)
// 6. Recorre la lista e imprime los valores finales
lista.traverse();