# operadores logicos

x = True
y = False
# print(x and y)  # AND
# print(x or y)  # OR
# print(not x)  # NOT


# ejemplos
# AND or &
resultado = True and True  # devolver true
resultado2 = False and True  # devuelve False
resultado3 = True and False  # devuelve False
resultado4 = False and False  # devuelve False

# OR o tambien '|'

resultado5 = True | True  # devolver True
resultado6 = True | False  # devolver True
resultado7 = False | True  # devolver True
resultado8 = False | False  # devolver False

# NOT

resultado9 = not True  # devolver False
resultado10 = not False  # devolver True


numero = int(input('Ingresa un numero '))

if numero > 0 and numero % 2 == 0:
    print("Tu numero es par y positivo")
elif numero < 0:
    print("Tu numero es negativo")
else:
    print("Tu numero no es par")


Usuario = input("Ingresa tu usuario")
contraseña = int(input("Ingresa tu usuario"))

if Usuario == "admin" and contraseña == "1234":
    if Usuario == contraseña:
        print("El usuario y contraseña no pueden ser iguales bruto de mierda")
    else:
        print("acceso concedido")
else:
    print("Usuario o contraseña incorrectos")
