
def suma():
    a = float(input("Ingrese un numero: "))
    b = float(input("Ingrese un numero: "))
    resultado = a + b
    print("El valor de la suma es: ", resultado)


def resta():
    a = float(input("Ingrese un numero: "))
    b = float(input("Ingrese un numero: "))
    resultado = a-b
    print("el valor de la resta es: ", resultado)


def multiplicacion():
    a = float(input("Ingrese un numero: "))
    b = float(input("Ingrese un numero"))
    resultado = a*b
    print("el valor de la multiplicacion es: ", resultado)


def division():
    a = float(input("Ingrese un numero: "))
    b = float(input("Ingrese un numero: "))
    if b == 0:
        print("No se puede dividir entre cero")
        return

    resultado = a/b

    print('resultado es', resultado)


def potencia():
    print("Potenciación")
    a = float(input("Ingrese la base: "))
    b = float(input('Ingrese la potencia: '))
    resultado = a**b
    print("El resultado es: ", resultado)


def raiz():
    n = float(input("Raiz que desea sacar"))
    Num = float(input('Numero dentro de la raiz'))

    if Num < 0 and n % 2 == 0:
        print('No se puede sacar raiz par de un numero negativo')

    resultado = pow(Num, 1/n)
    print("El resultado de la raíz es: ", resultado)


def calculadora():
    print("Seleccione una operacion: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print('5. Potenciacion')
    print('6. Raiz')


if __name__ == '__main__':
    calculadora()

opcion = input("Ingrese el numero de la opcion (1,2,3,4,5,6): ")


if opcion == '1':
    suma()
elif opcion == '2':
    resta()
elif opcion == '3':
    multiplicacion()
elif opcion == '4':
    division()
elif opcion == '5':
    potencia()
elif opcion == '6':
    raiz()
