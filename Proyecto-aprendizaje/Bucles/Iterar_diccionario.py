diccionario = {'Nombre': 'Tomas', 'Edad': 20, 'Ciudad': 'Madrid'}
#iterar en diccionarios usando for  
for key in diccionario: #por defecto itera en las claves
    print(f'Clave: {key}, Valor: {diccionario[key]}') #para acceder al valor usamos diccionario[clave]
    
#otra manera de obtener claves y valores usando .keys() y .values()
for clave in diccionario.items(): #usando .items() para obtener clave y valor juntos
    key = clave[0]
    value = clave[1]
    print(f'Clave: {key}, Valor: {value}') 

#para obtener solo keys
for key1 in diccionario:
    key
    print(f'Clave: {key1}')