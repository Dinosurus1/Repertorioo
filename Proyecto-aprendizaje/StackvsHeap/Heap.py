#ejemplo de Heap, las variables dinámicas se almacenan en el montón (heap)
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # atributo almacenado en el heap
        self.edad = edad      # atributo almacenado en el heap
persona1 = Persona("Ana", 30)  # objeto creado en el heap
print(f"Nombre: {persona1.nombre}, Edad: {persona1.edad}")
# Nota: Los objetos como 'persona1' se almacenan en el heap y permanecen allí hasta que no haya referencias a ellos, momento en el cual el recolector de basura los elimina.
#Otro ejemplo de uso de heap con listas
lista_numeros = [1, 2, 3, 4, 5]  # lista creada en el heap
lista_numeros.append(6)  # agregar un elemento a la lista
print(f"Lista de números: {lista_numeros}")
# Nota: Las listas y otros objetos dinámicos se almacenan en el heap y pueden crecer o cambiar de tamaño según sea necesario.
