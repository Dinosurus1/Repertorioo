


frase = input("Dime una frase y calculo cuanto tardarias en decirla")
# separa la frase en palabras y las guarda en una lista
palabras_separadas = frase.split(" ")
cantidad_de_palabras = len(frase)  # cuenta la cantidad de letras en la frase
# asumiendo que se dicen 5 letras por segundo
print(f"Dijiste {cantidad_de_palabras} palabras y tardarias {cantidad_de_palabras/5} segundos en decirla")
# asumiendo que se dicen 5 letras por segundo

# asumiendo que se dicen 5 letras por segundo y yo soy un 30% mas rapido
print(
    f"Yo soy un 30% mas rapido que tu lo hago en {cantidad_de_palabras/5*0.7} segundos")

if cantidad_de_palabras > 120:
    print("Eres un robot")
else:
    print("Eres humano")



