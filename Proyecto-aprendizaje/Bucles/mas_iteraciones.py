frutas = ["manzana", "banana", "cereza", "naranja", "pera", "uva", "kiwi", "mango", "papaya", "piña"]
for fruta in frutas:
    if fruta == "naranja":
        continue  # saltar la naranja
    print("Me gusta la", fruta)
#se salta la naranja y sigue con las demas frutas
#lo que hace el continue es saltar la iteracion actual y seguir con la siguiente
#ejemplo con break
for fruta in frutas:
    if fruta == "naranja":
        break  # salir del bucle al encontrar la naranja

else:
    print("Me gusta la", fruta)#el else no se ejecuta si hay un break
#se detiene al encontrar la naranja y no sigue con las demas frutas
#lo que hace el break es salir completamente del bucle 

#recorrer una cadena de texto
cadena = "Hola Mundo"
for caracter in cadena:
    print(caracter)
#recorre cada caracter de la cadena y lo imprime en una nueva linea

#metodo normal de duplicar valores en una lista
numeros=[1,2,3,4,5,6,7,8,9,10]
numeros_duplicado = list()
for numero in numeros: numeros_duplicado.append(numero * 2)
print(numeros_duplicado)
#crea una nueva lista con los numeros duplicados en una sola linea de codigo

#for en una solo linea de codigo
numeros_triplicados = [numero * 3 for numero in numeros]
print(numeros_triplicados)
#crea una nueva lista con los numeros triplicados en una sola linea de codigo usando listas por comprension
