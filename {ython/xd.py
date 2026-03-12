from datetime import date
from datetime import datetime, date

def calcular_edad(fecha_nac, fecha_act):
    # Convertir cadenas a objetos de tipo fecha
    nacimiento = datetime.strptime(fecha_nac, "%d/%m/%Y").date()
    actual = datetime.strptime(fecha_act, "%d/%m/%Y").date()

    # Calcular edad
    edad = actual.year - nacimiento.year

    # Ajustar si aún no ha cumplido años
    if (actual.month, actual.day) < (nacimiento.month, nacimiento.day):
        edad -= 1

    return edad

# --- Entrada de datos ---
print("=== Calcular edad actual ===")
fecha_nac = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
fecha_act = input("Ingrese la fecha actual (dd/mm/aaaa): ")

# --- Salida ---
print("La edad actual es:", calcular_edad(fecha_nac, fecha_act), "años")
