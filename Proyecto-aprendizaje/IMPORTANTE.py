# operadores aritmeticos

import math
a = 10
b = 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b
division_entera = a // b
potencia = a ** b
modulo = a % b
print("Suma: ", suma)
print("Resta: ", resta)
print("Multiplicacion: ", multiplicacion)
print("Division: ", division)
print("Division entera: ", division_entera)
print("Potencia: ", potencia)
print("Modulo: ", modulo)

# operadores de comparacion

print(a == b)  # igualdad
print(a != b)  # diferente
print(a > b)  # mayor que
print(a < b)  # menor que
print(a >= b)  # mayor o igual que
print(a <= b)  # menor o igual que

# calculos combinados
a = 5
b = 2
c = 3
comparacion = a + b * c > (a - b) ** c
print(comparacion)  # False

# comparar usuarios
usuario1 = "Daniel"
usuario2 = input("Ingrese el nombre del usuario 2: ")

if usuario1 == usuario2:
    print("Los usuarios son iguales")
else:
    print("Bienvenido ", usuario1) and print("Bienvenido ", usuario2)


# evaluar si las conntraseñas son iguales
contraseña_almacenada = "password123"
contraseña_ingresada = input("Ingrese su contraseña: ")

if contraseña_almacenada == contraseña_ingresada:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")

# operadores logicos

x = True
y = False
print(x and y)  # AND
print(x or y)  # OR
print(not x)  # NOT

# operadores de asignacion

c = 5
c += 3  # c = c + 3
print(c)
c -= 2  # c = c - 2
print(c)
c *= 4  # c = c * 4
print(c)
c /= 2  # c = c / 2
print(c)
c %= 3  # c = c % 3
print(c)
c **= 2  # c = c ** 2
print(c)
c //= 2  # c = c // 2
print(c)
# operadores de identidad
d = 10
e = 10
print(d is e)  # True si d y e son el mismo objeto
print(d is not e)  # False si d y e son el mismo objeto
# operadores de pertenencia
frutas = ["manzana", "banana", "cereza"]
print("banana" in frutas)  # True si "banana" esta en la lista frutas
print("pera" not in frutas)  # True si "pera" no esta en la lista frutas
# operadores bit a bit
f = 5  # en binario: 0101
g = 3  # en binario: 0011
print(f & g)  # AND bit a bit: 0001 -> 1
print(f | g)  # OR bit a bit: 0111 -> 7
print(f ^ g)  # XOR bit a bit: 0110 -> 6
print(~f)     # NOT bit a bit: 1010 -> -6
print(f << 1)  # Desplazamiento a la izquierda: 1010 -> 10
print(f >> 1)  # Desplazamiento a la derecha: 0010 -> 2
# operadores especiales
print(math.sqrt(16))  # Raiz cuadrada
print(abs(-7))        # Valor absoluto
print(round(3.6))     # Redondeo
print(pow(2, 3))      # Potencia
print(max(1, 5, 3))   # Maximo
print(min(1, 5, 3))   # Minimo
print(sum([1, 2, 3]))  # Suma de elementos en una lista
# operadores de cadena
cadena1 = "Hola"
cadena2 = "Mundo"
print(cadena1 + " " + cadena2)  # Concatenacion
print(cadena1 * 3)               # Repeticion
print("Hola" in cadena1)          # Pertenencia
print(cadena1[1])                # Indexacion
print(cadena1[1:3])              # Slicing
print(cadena1.lower())           # Minusculas
print(cadena1.upper())           # Mayusculas
print(cadena1.replace("o", "a"))  # Reemplazo
print(cadena1.split("o"))        # Division en lista
print(len(cadena1))              # Longitud
print(cadena1.startswith("H"))   # Comienza con
print(cadena1.endswith("a"))     # Termina con
print(cadena1.find("o"))         # Indice de primer ocurrencia
print(cadena1.count("o"))        # Cuenta ocurrencias
print(cadena1.isalpha())         # Solo letras
print(cadena1.isdigit())         # Solo digitos
print(cadena1.isspace())         # Solo espacios
print(cadena1.title())           # Titulo
print(cadena1.capitalize())      # Capitalizar
print(cadena1.center(10))        # Centrar
print(cadena1.ljust(10))         # Alinear a la izquierda
print(cadena1.rjust(10))         # Alinear a la derecha
print(cadena1.zfill(10))         # Rellenar con ceros a la izquierda
print(cadena1.encode())          # Codificar
print(cadena1.decode('utf-8'))   # Decodificar
print(cadena1.format())          # Formatear
print(f"{cadena1} Mundo")        # Formateo con f-strings
print(cadena1.islower())         # Todas minusculas
print(cadena1.isupper())         # Todas mayusculas
# Cambiar mayusculas por minusculas y viceversa
print(cadena1.swapcase())
print(cadena1.partition("o"))    # Particionar
print(cadena1.rpartition("o"))   # Particionar desde el final
print(cadena1.lstrip("H"))       # Eliminar caracteres a la izquierda
print(cadena1.rstrip("a"))       # Eliminar caracteres a la derecha
print(cadena1.strip("H"))        # Eliminar caracteres a ambos lados
print(cadena1.expandtabs(4))    # Expandir tabulaciones
print(cadena1.isprintable())     # Es imprimible
print(cadena1.maketrans("H", "J"))  # Crear tabla de traduccion
print(cadena1.translate(cadena1.maketrans("H", "J")))  # Traducir usando tabla
print(cadena1.encode('utf-8').decode('utf-8'))  # Codificar y decodificar
print(cadena1.removeprefix("H"))  # Eliminar prefijo
print(cadena1.removesuffix("a"))  # Eliminar sufijo
print(cadena1.isidentifier())    # Es un identificador valido
print(cadena1.isnumeric())       # Solo numeros
print(cadena1.isdecimal())       # Solo decimales
print(cadena1.isalnum())         # Solo alfanumerico
print(cadena1.join(["Hola", "Mundo"]))  # Unir lista con cadena como separador
print(cadena1.encode('utf-8'))   # Codificar a bytes
print(cadena1.decode('utf-8'))   # Decodificar de bytes a cadena
print(cadena1.casefold())        # Comparacion sin distincion de mayusculas
