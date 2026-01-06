animales = ['perro', 'gato','loro','cocodrilo']#listas
#print(animales)

#for animal in animales:#cuando uno pregunta a una lista normal print(animales) te dira el elemento de la lista en lista, con bucle for hacemos que pase por cada elemento de la lista
    #print(f'los animales son:{animal}') #bucle for crea una variable que hace que se repita tantas veces lo pidas


numeros = [54,12,412,65]

#for numero in numeros: #usamos el ciclo para guardar en nueva variable cada dato de lista y luego multiplicarla por 10 xd
    #resultado = numero * 10
   # print(resultado )

#como hacemos para iterar en 2 listas (Las listas tienen que ser del mismo size)
#usamos la funcion zip para nombrar las 2 listas
for numero,animal in zip(animales,numeros):
    print(f'recorriendo lista1: {numero}')
    print(f'recorriendo lista2: {animal}')

#usando la funcion in range
#forma incorreccta de recorrer una lista con su indice
for num in range(len(numeros)):#arranca en 5 termina en 10 (9) el 10 no lo cuenta si le decimos solo(20) ira de 0 al que se le diga -1

    print(numeros[num])
#este for si no funciona en conjuntos sapos 
#forma correcta de recorrer una lista con su indicie

for num in enumerate(numeros   ):
    indice = num[0]
    valor = num[1]
    print(f'el indice es: {indice} y el valor es: {valor}')

#usando el else

for number in numeros:
    print(f"Ejecutando el ultimo bucle, valor actual: {number}")
else:
    print('el bucle termino')#el else se muestra al final del bucle siempre

#si hay un break no se ejecuta\\
#todo funciona igual en tuplas listas y conjuntos 