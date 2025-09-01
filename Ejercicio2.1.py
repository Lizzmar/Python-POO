# Ejercicio Herencia
# Crear 3 clases animal mamifero y ave
# Animal metodo comer Mamifero amamantar Ave volar
# Clase Murcielago que herede de Mamifero y Ave 
# Jugar con el orden de herencia de la clase Muercielago

class Animal:
    def comer(self):
        print("El animal está comiendo.")


class Ave(Animal):
    def volar(self):
        print("El ave está volando.")

class Mamifero(Animal):
    def amamantar(self):
        print("El mamífero está amamantando.")


# Herencia múltiple: Murciélago hereda de Mamífero y Ave
class Murcielago(Mamifero, Ave):
    pass

# Prueba de los métodos y el orden de resolución
murcielago = Murcielago()

murcielago.comer()        # Heredado de Animal
murcielago.amamantar()    # Método de Mamífero
murcielago.volar()        # Método de Ave

# Cambiando orden de herencia y observando el efecto
class Murcielago2(Ave, Mamifero):
    pass

murcielago2 = Murcielago2()
murcielago2.comer()
murcielago2.amamantar()
murcielago2.volar()

ave=Ave()

ave.comer()
ave.volar()

print(Murcielago.mro())