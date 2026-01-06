verificacion_edad= int("Ingrese su edad: ")

if verificacion_edad >= 18: 
    print("Eres mayor de edad") #true
else: #false 
    print("No puedes ingresar, eres menor de edad")


#estructura if
# if condicion: Accion si se cumple la condicion
# else: Accion si no se cumple la condicion


Ingreso_mensual = float(input("Ingresa tu ingreso mensual"))
gastos_mensual = float(input("Ingresa tu gastos mensuales"))

if Ingreso_mensual - gastos_mensual <= 0:
    print("estas en la inmunda")