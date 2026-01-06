Credenciales = {
    "Daniel": {"contraseña": "Daniel123", "edad": 25}
}


while True:  # ciclo infinito para el menu
    print("Bienvenido al sistema de verificación de edad")
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Salir")
    opcion = input("Seleccione una opción (1, 2, 3): ")
    # registro del usuario
    if opcion == "1":
        print("Registro de nuevo usuario")
        # la lista de los usuarios registrados
        usuarios_registrados = list(Credenciales.keys())
        print("Usuarios registrados:", usuarios_registrados)
        usuario_nuevo = input(
            "Ingrese el nombre de usuario que desea registrar: ")
        while usuario_nuevo in Credenciales:  # este while verifica usuario_nuevo en Credenciales si ya esta en uno
            print(
                f"El nombre de usuario {usuario_nuevo} ya está en uso. Por favor, elija otro.")
            usuario_nuevo = input(
                "Ingrese el nombre de usuario que desea registrar: ")

        # Validar la edad del nuevo usuario
        while True:  # este while True otro infinito es para le verificacion de edas

            try:  # lo que hace el try es que si sucede un error dentro del bloque de codigo busca el 'except' para hacer lo que dice el except

                registro_edad = int(input("Ingrese su edad: "))

                # verificamos que la edad sea un numero positivo y no mayor a 100
                if registro_edad <= 0 or registro_edad > 100:
                    print(
                        "Por favor, ingrese una edad válida (número positivo menor a 100).")
                    continue  # continuamos el bucle para que vuelva a pedir la edad

                elif registro_edad <= 18:  # segunda validacion que sea mayor de edad
                    print("No puedes registrarte, eres menor de edad.")
                    break  # rompemos el bucle ya que no es mayor de edad

                else:
                    while True:  # este while true es lo mismo de la verificacion de edad solo que con contraseña y mas facil que el de edad ya que se puede cualquier caracter
                        usuario_contraseña = input(
                            "Ingrese la contraseña que desea registrar: ")
                        if usuario_contraseña == "":  # en caso de que pongan la contraseña vacia
                            print("La contraseña no puede estar vacía.")
                        elif usuario_contraseña == usuario_nuevo:  # si el usuario es pendejo y pone su contraseña igual al de usuario
                            print(
                                "La contraseña no puede ser igual al nombre de usuario.")
                        else:
                            # Guardar el nuevo usuario en el diccionario
                            Credenciales[usuario_nuevo] = {  # Guarda en credenciales [usuario_nuevo] y de ese usuario_nuevo guarda los valores contraseña que seria usuario_contraseña y lo mismo para edad
                                "contraseña": usuario_contraseña,
                                "edad": registro_edad
                            }
                            print(
                                f"¡Registro exitoso! Bienvenido {usuario_nuevo}.")
                            break
                    break  # rompe el ciclo while True

            except ValueError:
                print("Error: Ingrese un número válido para la edad.")

    elif opcion == "2":
        print("Inicio de sesion")
        usuario_login = input("Ingrese tu usuario")
        contraseña_login = input('Ingrese tu contraseña')

        if usuario_login in Credenciales:  # verifica si el usuario existe en el diccionario Credenciales*
            # accede al diccionario anidado para comparar la contraseña almacenada con la ingresada
            if Credenciales[usuario_login]["contraseña"] == contraseña_login:
                # si edad_usuario = a las credenciales del usuario entones imprima esto esto es simplemente para imprimir la edad del usuario y que verifique cual es la edad del usuario logueado xd
                edad_usuario = Credenciales[usuario_login]["edad"]
                print(
                    f"¡Inicio de sesión exitoso! Bienvenido {usuario_login}.")
                print(f"Edad registrada: {edad_usuario} años.")
            else:
                print("Contraseña incorrecta.")
        else:
            print("El usuario no existe.")

    elif opcion == "3":  # para romper el bucle while True
        print("Saliendo del programa. ¡Hasta luego!")
        break
    else:
        print("opcion no valida")  # para q no sea autista el usuario
