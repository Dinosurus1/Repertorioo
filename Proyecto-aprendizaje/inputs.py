nombre = input("Introduce tu nombre: ") # Solicita al usuario que introduzca su nombre y lo almacena en la variable 'nombre'
edad = int(input("Introduce tu edad: ")) # Solicita al usuario que introduzca su edad, la convierte a entero y la almacena en la variable 'edad'
altura = float(input("Introduce tu altura en metros: ")) # Solicita al usuario que introduzca su altura, la convierte a flotante y la almacena en la variable 'altura'
print (f"Hola {nombre}, tienes {edad} años y mides {altura} metros.") # Imprime un mensaje con el nombre, edad y altura del usuario
# Nota: input() siempre devuelve una cadena, por lo que es necesario convertirla a int o float si se requiere un tipo numérico.
# También se puede usar eval() para evaluar la entrada del usuario, pero es menos seguro y no se recomienda para entradas no confiables.
# el f al inicio de la cadena permite usar variables dentro de la cadena con {}
# Ejemplo: f"Hola {nombre}"

#ejemplo de usar int y float

numero1 = input("Introduce un número entero: ")
numero2 = input("Introduce un número decimal: ")

suma = int(numero1) + float(numero2)  # Convertir las entradas a int y float antes de sumar
print(f"La suma de {numero1} y {numero2} es: {suma}")