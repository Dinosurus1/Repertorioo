Credenciales = {  # se usa diccionario para guardar usuario y contraseñas # usuario:contraseña/keys:values

}
# usamos el while tru: para crear un bucle infinito con el menu de opciones
while True:
    print("\n------ Menú de Opciones -----")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
# opciones para elegir
    opcion = input('Selecciones una opcion (1, 2, 3): ')

# de aqui para abajo van las opciones los posible caso que puede elegir el usuario
    if opcion == '1':  # registro de nuevo usuario
        print("\n--- Registro de Nuevo Usuario ---")
        # obtiene los usuarios del diccionario
        Usuarios_registrados = list(Credenciales.keys())
        usuario_nuevo = input(
            "Ingrese el nombre de usuario que desea registrar: ")  # pide el nombre de usuario

        # el ciclo while verifica si el nombre de usuario ya esta en uso en el diccionario
        while usuario_nuevo in Usuarios_registrados:
            print(
                f"El nombre de usuario {usuario_nuevo} ya está en uso. Por favor, elija otro.")
            usuario_nuevo = input(
                "Ingrese el nombre de usuario que desea registrar: ")
        print(
            f"El nombre de usuario '{usuario_nuevo}' está disponible y ha sido registrado con éxito.")
        Usuario_contraseña = input(
            # pide la contraseña para registras
            "Ingrese la contraseña que desea registrar: ")
        while Usuario_contraseña == "":  # verifica que la contraseña no este vacia
            print("La contraseña no puede estar vacía. Por favor, intente de nuevo.")
            Usuario_contraseña = input(
                "Ingrese la contraseña que desea registrar: ")
        while Usuario_contraseña == usuario_nuevo:  # verifica que la contraseña no sea igual al nombre de usuario
            print(
                "La contraseña no puede ser igual al nombre de usuario. Por favor, intente de nuevo.")
            Usuario_contraseña = input(
                "Ingrese la contraseña que desea registrar: ")
        # agrega el nuevo usuario y contraseña al diccionario
        Credenciales[usuario_nuevo] = Usuario_contraseña

    elif opcion == '2':  # inicio de sesion una vez registrado
        print("\n--- Inicio de Sesión ---")
        usuario_login = input(
            "Ingrese su nombre de usuario para iniciar sesión: ")
        contraseña_login = input("Ingrese su contraseña para iniciar sesión: ")

        # el while verifica el inicio de sesion es decir el usuario y la contraseña que sean igual al que esta en el diccionario
        while usuario_login in Credenciales and Credenciales[usuario_login] == contraseña_login:
            print("Inicio de sesión exitoso.", "Bienvenido", usuario_login)
            break
        else:
            print("Nombre de usuario o contraseña incorrectos. Inténtelo de nuevo.")

    elif opcion == '3':  # salir del programa
        print("Saliendo del programa. ¡Hasta luego!")
        break
     # en caso de que eliga una opcion que nada que ver
    else:
        print("Opción no válida. Por favor, seleccione una opción del menú.")
