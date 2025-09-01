# Polimorfismo: la capacidad de diferentes objetos de responder al mismo método 
# de forma específica

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def hablar(self):
        # Método que será sobreescrito en clases derivadas
        pass

class Perro(Animal):
    def hablar(self):
        return "Guau"

class Gato(Animal):
    def hablar(self):
        return "Miau"

# Función que muestra el comportamiento polimórfico: 
# recibe un objeto de tipo Animal y llama a su método hablar
def escuchar_animal(animal):
    print(animal.nombre + " dice: " + animal.hablar())

# Crear instancias de Perro y Gato
perro = Perro("Bobby")
gato = Gato("Luna")

# Llamar la función pasando diferentes objetos
escuchar_animal(perro)  # Bobby dice: Guau
escuchar_animal(gato)   # Luna dice: Miau

# Polimorfismo con tipos de datos (enteros y strings) en una función
def sumar(obj1, obj2):
    return obj1 + obj2

print(sumar(5, 10))         # Suma números enteros: 15
print(sumar("Hola ", "Mundo"))  # Concatenación de strings: Hola Mundo

# Polimorfismo = Muchas formas y permite que diferentes clases implementen el mismo método de manera distinta.

#Aquí, las clases Perro y Gato heredan de Animal y redefinen el método hablar
