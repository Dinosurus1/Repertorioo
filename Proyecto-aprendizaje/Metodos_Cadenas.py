# operadores de cadena
cadena1 = "Hola"
cadena2 = "Mundo"
print(cadena1 + " " + cadena2)  # Concatenacion
print(cadena1 * 3)               # Repeticion
# Pertenencia # Devuelve True si "Hola" esta en cadena1
print("Hola" in cadena1)
# Indexacion # Devuelve 'o', el caracter en la posicion 1
print(cadena1[1])
# Slicing # Devuelve 'ol', desde la posicion 1 hasta la 3 (no incluye la 3)
print(cadena1[1:3])
# Minusculas # Convierte toda la cadena a minusculas
print(cadena1.lower())
# Mayusculas # Convierte toda la cadena a mayusculas
print(cadena1.upper())
# Reemplazo # Reemplaza 'o' por 'a', devuelve 'Hala'
print(cadena1.replace("o", "a"))
# Division en lista # Divide la cadena en una lista usando 'o' como separador, devuelve ['H', 'la']
print(cadena1.split("o"))
# Longitud # Devuelve la longitud de la cadena, en este caso 4
print(len(cadena1))
# Comienza con # Devuelve True si la cadena comienza con 'H'
print(cadena1.startswith("H"))
# Termina con # Devuelve True si la cadena termina con 'a'
print(cadena1.endswith("a"))
# Indice de primer ocurrencia buscar letra o palabra en la cadena
# Devuelve el indice de la primera ocurrencia de 'o', en este caso 1
print(cadena1.find("o"))
# Cuenta ocurrencias # Devuelve el numero de veces que 'o' aparece en la cadena, en este caso 1
print(cadena1.count("o"))
# Solo letras # Devuelve True si todos los caracteres son letras y la cadena no esta vacia
print(cadena1.isalpha())
# Solo digitos # Devuelve True si todos los caracteres son digitos y la cadena no esta vacia
print(cadena1.isdigit())
# Solo espacios # Devuelve True si todos los caracteres son espacios y la cadena no esta vacia
print(cadena1.isspace())
# Titulo # Convierte la primera letra de cada palabra a mayuscula
print(cadena1.title())

# Capitalizar primera letra mayus y vuelve todo minuscula
print(cadena1.capitalize())
# Centrar # Centra la cadena en un campo de ancho 10, rellenando con espacios
print(cadena1.center(10))
# Alinear a la izquierda # Alinea la cadena a la izquierda en un campo de ancho 10, rellenando con espacios
print(cadena1.ljust(10))
# Alinear a la derecha # Alinea la cadena a la derecha en un campo de ancho 10, rellenando con espacios
print(cadena1.rjust(10))
# Rellenar con ceros a la izquierda # Rellena la cadena con ceros a la izquierda hasta alcanzar un ancho de 10
print(cadena1.zfill(10))
# Codificar67         # Codifica la cadena a bytes usando UTF-8
print(cadena1.encode())
# print(cadena1.decode('utf-8'))   # Decodificar # Decodifica bytes a cadena usando UTF-8 (esto dara error si cadena1 no es bytes)
# Formatear # Devuelve la cadena formateada (en este caso no cambia nada)
print(cadena1.format())
print(f"{cadena1} Mundo")        # Formateo con f-strings
print(cadena1.islower())         # Todas minusculas
# Todas mayusculas  # Cambiar mayusculas por minusculas y viceversa
print(cadena1.isupper())

print(cadena1.swapcase())
# Particionar # Divide la cadena en una tupla en la primera ocurrencia de 'o', devuelve ('H', 'o', 'la')
print(cadena1.partition("o"))
# Particionar desde el final # Divide la cadena en una tupla en la ultima ocurrencia de 'o', devuelve ('H', 'o', 'la')
print(cadena1.rpartition("o"))
# Eliminar caracteres a la izquierda # Elimina 'H' del inicio de la cadena, devuelve 'ola'
print(cadena1.lstrip("H"))
# Eliminar caracteres a la derecha # Elimina 'a' del final de la cadena, devuelve 'Hol'
print(cadena1.rstrip("a"))
# Eliminar caracteres a ambos lados # Elimina 'H' del inicio y final de la cadena, devuelve 'ola'
print(cadena1.strip("H"))
# Expandir tabulaciones # Reemplaza tabulaciones por espacios (4 espacios por tabulacion)
print(cadena1.expandtabs(4))
# Es imprimible # Devuelve True si todos los caracteres son imprimibles o la cadena esta vacia
print(cadena1.isprintable())
# Crear tabla de traduccion # Crea una tabla de traduccion para reemplazar 'H' por 'J'
print(cadena1.maketrans("H", "J"))
# Traducir usando tabla # Usa la tabla de traduccion para reemplazar 'H' por 'J', devuelve 'Jola'
print(cadena1.translate(cadena1.maketrans("H", "J")))
# Codificar y decodificar # Codifica a bytes y luego decodifica de nuevo a cadena
print(cadena1.encode('utf-8').decode('utf-8'))
print(cadena1.removeprefix("H"))  # Eliminar prefijo
print(cadena1.removesuffix("a"))  # Eliminar sufijo
# Es un identificador valido # Devuelve True si la cadena es un identificador valido en Python
print(cadena1.isidentifier())
print(cadena1.isnumeric())       # Solo numeros
print(cadena1.isdecimal())       # Solo decimales
print(cadena1.isalnum())         # Solo alfanumerico
print(cadena1.join(["Hola", "Mundo"]))  # Unir lista con cadena como separador
print(cadena1.encode('utf-8'))   # Codificar a bytes
print(cadena1.decode('utf-8'))   # Decodificar de bytes a cadena
# Comparacion sin distincion de mayusculas # Convierte la cadena a una forma que permite comparaciones sin distincion de mayusculas
print(cadena1.casefold())
# ejemplos de uso de startswith y endswith con input
texto = input("Ingresa un texto: ")
if texto .startswith("H"):
    print("el texto comienza con H")
else:
    print("el texto no comienza con H")
if texto.endswith("a"):
    print("el texto termina con a")
else:
    print("el texto no termina con a")

# ejemplo de uso de isdigit con input
numero = input("Ingresa un numero: ")
if numero.isdigit():
    print("es un numero")
else:
    print("no es un numero")
# ejemplo de uso de isalpha con input
palabra = input("Ingresa una palabra: ")
if palabra.isalpha():
    print("es una palabra")
else:
    print("no es una palabra")
# ejemplo de uso de isalnum con input
cadena = input("Ingresa una cadena: ")
if cadena.isalnum():
    print("es alfanumerica")
else:
    print("no es alfanumerica")
# ejemplo de uso de isspace con input
espacios = input("Ingresa una cadena de espacios: ")
if espacios.isspace():
    print("solo contiene espacios")
else:
    print("no solo contiene espacios")
# ejemplo de uso de islower y isupper con input
texto2 = input("Ingresa un texto: ")
if texto2.islower():
    print("todo en minusculas")
elif texto2.isupper():
    print("todo en mayusculas")
else:
    print("mezcla de mayusculas y minusculas")
# ejemplo de uso de join con input
lista = input("Ingresa varias palabras separadas por comas: ").split(",")
separador = input("Ingresa un separador: ")
resultado = separador.join(lista)
print("Cadena resultante:", resultado)
# ejemplo de uso de split con input
frase = input("Ingresa una frase: ")
palabras = frase.split(" ")
print("Palabras en la frase:", palabras)
# ejemplo de uso de replace con input
frase2 = input("Ingresa una frase: ")
vieja = input("Ingresa la palabra a reemplazar: ")
nueva = input("Ingresa la nueva palabra: ")
frase_modificada = frase2.replace(vieja, nueva)
print("Frase modificada:", frase_modificada)
# ejemplo de uso de strip con input
texto3 = input("Ingresa un texto con espacios al inicio y al final: ")
texto_limpio = texto3.strip()
print("Texto sin espacios:", texto_limpio)
# ejemplo de uso de format y f-strings con input
nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
print("Hola, {}. Tienes {} años.".format(nombre, edad))
print(f"Hola, {nombre}. Tienes {edad} años.")
# ejemplo de uso de encode y decode con input
texto4 = input("Ingresa un texto: ") 
texto_codificado = texto4.encode('utf-8') 
print("Texto codificado:", texto_codificado)
texto_decodificado = texto_codificado.decode('utf-8')
print("Texto decodificado:", texto_decodificado) 
# ejemplo de uso de find y count con input
frase3 = input("Ingresa una frase: ") 
palabra_buscar = input("Ingresa la palabra a buscar: ")
indice = frase3.find(palabra_buscar) 
ocurrencias = frase3.count(palabra_buscar)
if indice != -1:
    print(f"La palabra '{palabra_buscar}' se encuentra en el indice {indice}.")
else:
    print(f"La palabra '{palabra_buscar}' no se encuentra en la frase.")
print(f"La palabra '{palabra_buscar}' aparece {ocurrencias} veces en la frase.")
# ejemplo de uso de isprintable con input
texto5 = input("Ingresa un texto: ")
if texto5.isprintable():
    print("El texto es imprimible.")
else:
    print("El texto no es imprimible.")
# ejemplo de uso de isidentifier con input
identificador = input("Ingresa un posible identificador: ")
if identificador.isidentifier():
    print("Es un identificador valido en Python.")
else:
    print("No es un identificador valido en Python.")
# ejemplo de uso de isnumeric e isdecimal con input
numero2 = input("Ingresa un numero: ")
if numero2.isnumeric():
    print("Es un numero (isnumeric).")
else:
    print("No es un numero (isnumeric).")
if numero2.isdecimal():
    print("Es un numero decimal (isdecimal).")
else:
    print("No es un numero decimal (isdecimal).")
# ejemplo de uso de zfill con input
numero3 = input("Ingresa un numero: ")
ancho = int(input("Ingresa el ancho total (incluyendo ceros): "))
numero_relleno = numero3.zfill(ancho) # Rellena con ceros a la izquierda hasta alcanzar el ancho especificado ejemplo: si el numero es 42 y el ancho es 5, el resultado sera 00042
print("Numero con ceros a la izquierda:", numero_relleno)
# ejemplo de uso de center, ljust y rjust con input
texto6 = input("Ingresa un texto: ")
ancho2 = int(input("Ingresa el ancho total: "))
print("Texto centrado:", texto6.center(ancho2))
print("Texto alineado a la izquierda:", texto6.ljust(ancho2))
print("Texto alineado a la derecha:", texto6.rjust(ancho2))
# ejemplo de uso de swapcase y title con input
texto7 = input("Ingresa un texto: ")
print("Texto con mayusculas y minusculas invertidas:", texto7.swapcase())
print("Texto en formato titulo:", texto7.title())
# ejemplo de uso de removeprefix y removesuffix con input
texto8 = input("Ingresa un texto: ")
prefijo = input("Ingresa el prefijo a eliminar: ")
sufijo = input("Ingresa el sufijo a eliminar: ")
texto_sin_prefijo = texto8.removeprefix(prefijo)
texto_sin_sufijo = texto8.removesuffix(sufijo)
print("Texto sin prefijo:", texto_sin_prefijo)
print("Texto sin sufijo:", texto_sin_sufijo)

