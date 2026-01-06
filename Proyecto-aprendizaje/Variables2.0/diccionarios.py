#creando diccionarios con dict (), diccionarios vacios con dict
diccionario = dict(nombre= 'Tomas', Edad = 'Sapo')
#Listas no pueden ser claves y usamos frozenset para meter conjuntos
diccionario1 = {frozenset(['daniel','rancio']):'XD'}
#creando diccionario con fromkeys (con todos los valores nones)

diccionario2= dict.fromkeys (['Nombre', 'Apellido']) #cuando lo pongo en modo []lista podremos poner varios valores
#si ponemos normal el fromkeys () sin los parentesis de lista seria el value none ya que los diccionarios son keys:values

#ejemplo:

diccionario3 = dict.fromkeys (["Nombre", "Apellido"], 'Ola')#ahora el valor sera Ola y no None es decir Nombre : Ola y Apellido: Ola le cambiamos el valor
#si lo ponemos sin lista es decir sin [] y ponemos ("Daniel", "Valorxd") asi na mas al imprimir daria:
diccionario4= dict.fromkeys("SAPOS", "Tomas")
print(diccionario4) #veremos como ser