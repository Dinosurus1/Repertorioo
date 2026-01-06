lista = list([1, 2, 3, 4, 5])  # crear una lista con la función list()

cadena = "Hola Mundo"
cantidad_elementos = len(lista)  # calcular la longitud de una cadena

# agregando un elemento a la lista
# agegando con appen

lista.append(6)  # agregar un elemento al final de la lista

# agregando un elemento a la lista a un indice específico

lista.insert(0, 0)  # agregar un elemento en el indice 0

# agregar varios elementos a la lista
lista.extend([7, 8, 9])  # agregar varios elementos al final de la lista

# eliminar un elemento de la lista por su indice


lista.pop(2)  # eliminar el elemento en el indice 2
# eliminar el último elemento de la lista con -2 elimina el penúltimo y asi con los demas
lista.pop(-1)

# eliminar un elemento de la lista por su valor

# eliminar el primer elemento con valor 4 con valores de texto es ""
lista.remove(4)

# eliminar todos los elementos de la lista

# lista.clear() #eliminar todos los elementos de la lista

# ordenar lista de forma ascendente

# ordenar la lista de forma ascendente con reverse=True se ordena de forma descendente
lista.sort(reverse=True)
# lista.sort() #ordenar la lista de forma ascendente

# invertir el orden de la lista
lista.reverse()  # invertir el orden de la lista casi igual a sort pero sin ordenar la lista

# verificar si un elemento está en la lista
existe = 3 in lista  # verificar si el elemento 3 está en la lista
# obtener el índice del elemento 3 en la lista
# obtener el índice del elemento 3 en la lista
elemento_encontrado = lista.index(6)
print(elemento_encontrado)
print(lista)
