#ejemplo de uso de stack, las variables locales se almacenan en la pila (stack)
def funcion_ejemplo():
    a = 10  # variable local almacenada en el stack
    b = 20  # variable local almacenada en el stack
    suma = a + b  # operación con variables locales
    return suma  # retorna la suma de a y b
resultado = funcion_ejemplo()
print(f"El resultado de la suma es: {resultado}")
# Nota: Las variables locales como 'a', 'b' y 'suma' se almacenan en el stack y se eliminan cuando la función termina su ejecución.
#otro ejemplo de uso de stack con recursión
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)  # llamada recursiva
numero = 5
resultado_factorial = factorial(numero)
print(f"El factorial de {numero} es: {resultado_factorial}")
# Nota: Cada llamada recursiva crea un nuevo marco en el stack, y cuando la función termina, esos marcos se eliminan del stack.
#es decir basicamente el stack es para variables locales y el heap para variables dinámicas como objetos y listas.