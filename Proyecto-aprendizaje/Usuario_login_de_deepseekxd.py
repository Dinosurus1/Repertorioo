Credenciales = {
    "Daniel": {"contraseña": "Daniel123", "edad": 25}
}


def mostrar_menu_principal():
    """Función que muestra el menú principal"""
    print("\n" + "="*50)
    print("       SISTEMA DE VERIFICACIÓN DE EDAD")
    print("="*50)
    print("1. Registrar nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Ver usuarios registrados")
    print("4. Salir")
    print("-"*50)


def mostrar_titulo_seccion(titulo):
    """Función para mostrar títulos de secciones"""
    print("\n" + "-"*30)
    print(f" {titulo}")
    print("-"*30)


def pausa():
    """Función para pausar y esperar entrada del usuario"""
    input("\nPresione Enter para continuar...")


def limpiar_pantalla():
    """Función para simular limpieza de pantalla"""
    print("\n" * 50)  # Imprime 50 líneas en blanco


def registrar_usuario():
    """Función para registrar un nuevo usuario"""
    mostrar_titulo_seccion("REGISTRO DE USUARIO")

    # Mostrar usuarios existentes
    usuarios_registrados = list(Credenciales.keys())
    print(
        f"Usuarios actuales: {', '.join(usuarios_registrados) if usuarios_registrados else 'No hay usuarios registrados'}")

    # Solicitar nombre de usuario
    usuario_nuevo = input(
        "\nIngrese el nombre de usuario que desea registrar: ")

    # Verificar si el usuario ya existe
    while usuario_nuevo in Credenciales:
        print(
            f"❌ El usuario '{usuario_nuevo}' ya existe. Por favor, elija otro.")
        usuario_nuevo = input(
            "Ingrese el nombre de usuario que desea registrar: ")

    # Validar edad
    while True:
        try:
            print("\n--- VERIFICACIÓN DE EDAD ---")
            registro_edad = int(input("Ingrese su edad: "))

            if registro_edad <= 0 or registro_edad > 100:
                print("❌ Edad inválida. Debe ser entre 1 y 100 años.")
            elif registro_edad < 18:
                print("❌ No puedes registrarte, eres menor de edad.")
                return  # Termina la función si es menor de edad
            else:
                break  # Edad válida, continuar

        except ValueError:
            print("❌ Error: Debe ingresar un número válido.")

    # Validar contraseña
    while True:
        print("\n--- REGISTRO DE CONTRASEÑA ---")
        usuario_contraseña = input(
            "Ingrese la contraseña que desea registrar: ")

        if usuario_contraseña == "":
            print("❌ La contraseña no puede estar vacía.")
        elif usuario_contraseña == usuario_nuevo:
            print("❌ La contraseña no puede ser igual al nombre de usuario.")
        elif len(usuario_contraseña) < 4:
            print("❌ La contraseña debe tener al menos 4 caracteres.")
        else:
            # Confirmar contraseña
            confirmacion = input("Confirme su contraseña: ")
            if usuario_contraseña != confirmacion:
                print("❌ Las contraseñas no coinciden. Intente nuevamente.")
            else:
                break

    # Guardar el nuevo usuario
    Credenciales[usuario_nuevo] = {
        "contraseña": usuario_contraseña,
        "edad": registro_edad
    }

    print(f"\n✅ ¡Registro exitoso! Bienvenido {usuario_nuevo}.")
    print(f"   Edad registrada: {registro_edad} años")


def iniciar_sesion():
    """Función para iniciar sesión"""
    mostrar_titulo_seccion("INICIO DE SESIÓN")

    if not Credenciales:
        print("❌ No hay usuarios registrados en el sistema.")
        return

    usuario_login = input("Usuario: ")
    contraseña_login = input("Contraseña: ")

    if usuario_login in Credenciales:
        if Credenciales[usuario_login]["contraseña"] == contraseña_login:
            edad_usuario = Credenciales[usuario_login]["edad"]
            print(f"\n✅ ¡Inicio de sesión exitoso!")
            print(f"   Bienvenido: {usuario_login}")
            print(f"   Edad registrada: {edad_usuario} años")

            # Menú después del login (podrías expandir esto)
            print(f"\n¿Qué deseas hacer, {usuario_login}?")
            print("1. Ver mi información")
            print("2. Cerrar sesión")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                print(f"\n--- INFORMACIÓN DE USUARIO ---")
                print(f"Nombre: {usuario_login}")
                print(f"Edad: {edad_usuario} años")
                print(
                    f"Estado: {'Mayor de edad' if edad_usuario >= 18 else 'Menor de edad'}")
        else:
            print("❌ Contraseña incorrecta.")
    else:
        print("❌ El usuario no existe.")


def mostrar_usuarios():
    """Función para mostrar usuarios registrados (sin contraseñas)"""
    mostrar_titulo_seccion("USUARIOS REGISTRADOS")

    if not Credenciales:
        print("No hay usuarios registrados.")
        return

    print(f"Total de usuarios: {len(Credenciales)}")
    print("\nLista de usuarios:")
    for i, usuario in enumerate(Credenciales.keys(), 1):
        edad = Credenciales[usuario]["edad"]
        print(f"  {i}. {usuario} - {edad} años")


# PROGRAMA PRINCIPAL
while True:
    limpiar_pantalla()
    mostrar_menu_principal()

    opcion = input("Seleccione una opción (1-4): ").strip()

    if opcion == "1":
        limpiar_pantalla()
        registrar_usuario()
        pausa()

    elif opcion == "2":
        limpiar_pantalla()
        iniciar_sesion()
        pausa()

    elif opcion == "3":
        limpiar_pantalla()
        mostrar_usuarios()
        pausa()

    elif opcion == "4":
        print("\n" + "="*50)
        print("    ¡Gracias por usar nuestro sistema!")
        print("              ¡Hasta luego! 👋")
        print("="*50)
        break

    else:
        print("❌ Opción no válida. Por favor seleccione 1-4.")
        pausa()
