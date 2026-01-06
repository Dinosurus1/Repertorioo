
# las listas son mutables se pueden modificar sus elementos
Lista = ["Manzana", "Banana", "Cereza", "Dátil"]
# la tupla es inmutable no se pueden modificar sus elementos
tupla = ["Pera", "Kiwi", "Piña", "Sexo"]
# modificar un elemento de la lista
Lista[3] = "Naranja"
print(Lista)

# esto no se puede hacer:
# tupla [2] = "Mango"
# creando un conjunto (set) (datos desordenados)
# podemos modicar los conjuntos, pero no podemos acceder a sus elementos por indice
conjunto = {"Rojo", "Verde", "Azul"}
# los conjuntos no permiten almacenar elementos duplicados
conjunto = {"Rojo", "Verde", "Azul", "Rojo"}
print(conjunto)
# print(conjunto[1]) -> no se puede acceder al elemento


# diccionario (estructura de datos que almacena pares clave-valor)
# se separan por comas y van entre llaves
diccionario = {
    "Nombre": "Juan",  # clave: valor
    "Edad": 30,
    "Ciudad": "Madrid",
    'Altura': 1.84,
    'Peso': 80
}

print(diccionario['Nombre'])  # Acceder a un valor por su clave
