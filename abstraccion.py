#  cumple la función de ocultar los detalles complejos o irrelevantes
# mostrando solo las características y comportamientos esenciales
class Auto:
    def __init__(self):
        # Atributo privado que almacena el estado del auto
        self.__estado = "apagado"
    
    def encender(self):
        # Cambia el estado a encendido y muestra mensaje
        self.__estado = "encendido"
        print("El auto está encendido")
    
    def conducir(self):
        # Si el auto está apagado, primero lo enciende
        if self.__estado == "apagado":
            self.encender()
        print("Conduciendo el auto")

# Crear una instancia de Auto
mi_auto = Auto()
mi_auto.conducir()  # Si está apagado, se enciende antes y luego conduce
#se abstraen (encender, apagar y conducir), pero los detalles internos no se muestran ni son necesarios para usar la clase.