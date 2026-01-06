cuenta_bancaria = {  # keys:values
    "titular": "Juan Pérez",
    "saldo": 1500,
    "moneda": "USD"
}

# obtener el valor asociado a la clave "titular"
# es mejor usar el .get porque si la clave no existe no da error
claves1 = cuenta_bancaria.get("titular")
claves2 = cuenta_bancaria["titular"]  # si la clave no existe da error
# obtener las claves del diccionario
# obtener las claves del diccionario (Tambien sirve para iterar)
claves = cuenta_bancaria.keys()
valores = cuenta_bancaria.values()  # obtener los valores del diccionario
# obtener los elementos (pares clave-valor) del diccionario
elementos = cuenta_bancaria.items() #recorre tanto claves como valores
# verificar si una clave está en el diccionario
# verificar si la clave "saldo" está en el diccionario
existe = "saldo" in cuenta_bancaria
# agregar o actualizar un elemento en el diccionario
cuenta_bancaria["saldo"] = 2000  # actualizar el saldo a 2000
# agregar una nueva clave "tipo_cuenta"
cuenta_bancaria["tipo_cuenta"] = "Ahorros"
# eliminar un elemento del diccionario por su clave
del cuenta_bancaria["moneda"]  # eliminar la clave "moneda"
# eliminar y obtener un elemento del diccionario por su clave
# eliminar y obtener el valor de la clave "saldo"
saldo = cuenta_bancaria.pop("saldo")#guarda el valor eliminado en la variable saldo
#eliminar todos los elementos del diccionario
# cuenta_bancaria.clear() #eliminar todos los elementos del diccionario


print(cuenta_bancaria)
