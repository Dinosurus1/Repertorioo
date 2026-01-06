import tkinter as tk
from tkinter import messagebox

def leer_numeros():
    """Lee y convierte los valores de los Entry a float. Lanza ValueError si no son números."""
    a_str = entry_x.get().strip()
    b_str = entry_y.get().strip()

    # opcional: permitir coma decimal reemplazándola por punto
    a_str = a_str.replace(',', '.')
    b_str = b_str.replace(',', '.')

    a = float(a_str)  # puede lanzar ValueError
    b = float(b_str)
    return a, b

def mostrar_resultado(texto):
    label_result.config(text=texto)

def manejar_error(e):
    # Mensaje amigable en un cuadro de diálogo y en la etiqueta de resultado
    messagebox.showerror("Error", str(e))
    mostrar_resultado("Error: " + str(e))

def suma():
    try:
        a, b = leer_numeros()
        res = a + b
        mostrar_resultado(f"Resultado: {res}")
    except ValueError:
        manejar_error("Ingrese números válidos.")
    except Exception as e:
        manejar_error(f"Error inesperado: {e}")

def resta():
    try:
        a, b = leer_numeros()
        res = a - b
        mostrar_resultado(f"Resultado: {res}")
    except ValueError:
        manejar_error("Ingrese números válidos.")
    except Exception as e:
        manejar_error(f"Error inesperado: {e}")

def multiplicacion():
    try:
        a, b = leer_numeros()
        res = a * b
        mostrar_resultado(f"Resultado: {res}")
    except ValueError:
        manejar_error("Ingrese números válidos.")
    except Exception as e:
        manejar_error(f"Error inesperado: {e}")

def division():
    try:
        a, b = leer_numeros()
        if b == 0:
            raise ZeroDivisionError("No se puede dividir entre cero.")
        res = a / b
        mostrar_resultado(f"Resultado: {res}")
    except ValueError:
        manejar_error("Ingrese números válidos.")
    except ZeroDivisionError as zde:
        manejar_error(str(zde))
    except Exception as e:
        manejar_error(f"Error inesperado: {e}")

def limpiar():
    entry_x.delete(0, tk.END)
    entry_y.delete(0, tk.END)
    mostrar_resultado("")

def salir():
    ventana.destroy()

# ---------- Interfaz ----------
ventana = tk.Tk()
ventana.title("Calculadora simple")
ventana.geometry("720x480")
ventana.resizable(False, False)  # opcional

# Etiquetas y entradas
label_x = tk.Label(ventana, text="Número 1:")
label_x.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_x = tk.Entry(ventana, width=18)
entry_x.grid(row=0, column=1, padx=5, pady=10)

label_y = tk.Label(ventana, text="Número 2:")
label_y.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_y = tk.Entry(ventana, width=18)
entry_y.grid(row=1, column=1, padx=5, pady=5)

# Botones de operaciones
frame_botones = tk.Frame(ventana)
frame_botones.grid(row=2, column=0, columnspan=2, pady=10)

btn_suma = tk.Button(frame_botones, text="Suma", width=10, command=suma)
btn_suma.grid(row=0, column=0, padx=5)

btn_resta = tk.Button(frame_botones, text="Resta", width=10, command=resta)
btn_resta.grid(row=0, column=1, padx=5)

btn_mul = tk.Button(frame_botones, text="Multiplicar", width=10, command=multiplicacion)
btn_mul.grid(row=0, column=2, padx=5)

btn_div = tk.Button(frame_botones, text="Dividir", width=10, command=division)
btn_div.grid(row=0, column=3, padx=5)

# Resultado
label_result = tk.Label(ventana, text="", font=("Arial", 12), fg="blue")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

# Botones inferiores: Limpiar y Salir
btn_limpiar = tk.Button(ventana, text="Limpiar", width=12, command=limpiar)
btn_limpiar.grid(row=4, column=0, pady=5)

btn_salir = tk.Button(ventana, text="Salir", width=12, command=salir)
btn_salir.grid(row=4, column=1, pady=5)

# Bind: pulsar Enter ejecuta suma (puedes cambiarlo)
def on_enter(event):
    suma()
ventana.bind('<Return>', on_enter)

# Ejecutar GUI
ventana.mainloop()
