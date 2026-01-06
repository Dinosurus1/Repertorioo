#creando un cojunto con set
#no son modificables
conjunto = set(["dato", 'dato2'])
#metiendo un cojunto dentro de otro conjunto

conjunto1 = frozenset({"dato1", 'dato2'})
conjunto2 = {conjunto1, 'dato3'}
print(conjunto2) #usar la funcion frozenset que hace modificable el conjunto para poderlo fucionar con otro conjunto

#Teoria de conjuntos

conjunto3 = {1,3,5,7}
conjunto4 = {1,3,7}
#usamos .issubset diciendo que si conjunto2 es subconjunto de conjunto 1 y nos botara True

resultado = conjunto4.issubset(conjunto3) #forma de verificarlo con issubset
resultado2 = conjunto2 <= conjunto1 #otra forma de verificarlo esto solo devuelve valores booleanos (True,False) y no es por la suma putos de mierda
#verificacion si es super conjunto ya no SUB

resultado3= conjunto4.issuperset(conjunto3) #con superset si 4 es super conjunto de 3 va a botar False porque 3 es el superconjunto no 4
resultado4 = conjunto4 > conjunto3 #verificando tambien si es superconjunto pero con signo "<>"

#Verificiar si hay algun numero en comun
resultado5= conjunto3.isdisjoint(conjunto4) #Va a botar False esto hace que compara los 2 conjuntos y si tienen numero igual botara false ya q no son diferentes.
#si los conjuntos fueran diferentes botaria True porque serian conjuntos diferentes
#print(resultado5)  


#como llamar a un valor del conjunto esto se llamaria iterar (lo veremos con los bucles)