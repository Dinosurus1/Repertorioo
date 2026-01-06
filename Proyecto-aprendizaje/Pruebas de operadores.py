Credenciales = {  # usuario:contraseña   recordar que el orden del diccionario es key:valor # en este caso usuario:contraseña
    "Daniel": "Daniel123",
    "Juan": "Juan123",
    "Pedro": "Pedro123",
    "Maria": "Maria123",
    "Ana": "Ana123",
}
# sabiendo que key:valor es usuario:contraseña la parte de Usuarios_registrados es para obtener los usuarios con el .keys()
# Obtener la lista de usuarios registrados
Usuarios_registrados = list(Credenciales.keys())
# Mostrar los usuarios registrados
print("Usuarios registrados:", Usuarios_registrados)
# registro de nuevo usuario
usuario_nuevo = input("Ingrese el nombre de usuario que desea registrar: ")


# Usar un bucle while para verificar si el nombre de usuario ya está en uso
while usuario_nuevo in Usuarios_registrados:  # le puse in porque lo hice mas avanzado    #aca se usa el operador de igualdad ==, pero tambien podemos usar un "in" en caso de que Usuarios_registrados sea una lista o cadena con varios nombres
    print(
        "El nombre de usuario {usuario_nuevo} ya está en uso. Por favor, elija otro.")
    usuario_nuevo = input("Ingrese el nombre de usuario que desea registrar: ")
print(
    f"El nombre de usuario '{usuario_nuevo}' está disponible y ha sido registrado con éxito.")
# puse int porque las contraseñas en el diccionario son numeros, si fueran letras no haria falta poner int
Usuario_contraseña = input("Ingrese la contraseña que desea registrar: ")
Credenciales[usuario_nuevo] = Usuario_contraseña  # Agregar el nuevo usuario

# Actualizar la lista de usuarios registrados
Usuarios_registrados = list(Credenciales.keys())
print("Usuarios registrados actualizados:", Usuarios_registrados)

# Verificar las credenciales de inicio de sesión
usuario_login = input("Ingrese su nombre de usuario para iniciar sesión: ")
contraseña_login = input("Ingrese su contraseña para iniciar sesión: ")
if usuario_login in Credenciales and Credenciales[usuario_login] == contraseña_login:
    print("Inicio de sesión exitoso.", "Bienvenido", usuario_login)
