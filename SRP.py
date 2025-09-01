# Una clase debe tener una única responsabilidad y por lo tanto una sola razón para cambiar.
class TanqueDeCombustible:
    # Separación clara de responsabilidades
    def __init__(self):
        # Inicializa el tanque con 100 litros de combustible
        self.combustible = 100

    def agregar_combustible(self, cantidad):
        # Añade la cantidad a combustible disponible
        self.combustible += cantidad

    def obtener_combustible(self):
        # Devuelve la cantidad actual de combustible
        return self.combustible

    def usar_combustible(self, cantidad):
        # Resta la cantidad usada de combustible
        self.combustible -= cantidad

class Auto:
    def __init__(self, tanque):
        # El auto tiene una posición y un tanque asociado
        self.posicion = 0
        self.tanque = tanque

    def mover(self, distancia):
        # El auto se mueve solo si tiene suficiente combustible
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print("Has movido el auto exitosamente")
        else:
            print("No hay suficiente combustible")

    def obtener_posicion(self):
        # Devuelve la posición actual del auto
        return self.posicion

# Ejemplo de uso
tanque = TanqueDeCombustible()
autito = Auto(tanque)

print(autito.obtener_posicion())
autito.mover(10)
print(autito.obtener_posicion())
autito.mover(20)
print(autito.obtener_posicion())
autito.mover(60)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
autito.mover(100)
print(autito.obtener_posicion())
