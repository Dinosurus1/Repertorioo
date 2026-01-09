#ejemplo de uso de stack, las variables locales se almacenan en la pila (stack)
def funcion_ejemplo():
    a = 10  # variable local almacenada en el stack
    b = 20  # variable local almacenada en el stack
    suma = a + b  # operación con variables locales
    return suma  # retorna la suma de a y b
resultado = funcion_ejemplo()
print(f"El resultado de la suma es: {resultado}")
# Nota: Las variables locales como 'a', 'b' y 'suma' se almacenan en el stack y se eliminan cuando la función termina su ejecución.
