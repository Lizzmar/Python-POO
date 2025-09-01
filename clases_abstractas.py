from abc import ABC, abstractmethod #Proporciona herramientas para crear clases abstractas y métodos abstractos.

# Clase abstracta Persona
class Persona(ABC):
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @abstractmethod
    def estudiar(self):
        # Método abstracto que debe implementar cualquier subclase
        pass

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}")

# Clase concreta Estudiante que hereda de Persona
class Estudiante(Persona):
    def __init__(self, nombre, edad, carrera):
        super().__init__(nombre, edad)
        self.carrera = carrera

    # Implementación obligatoria del método abstracto
    def estudiar(self):
        print(f"{self.nombre} está estudiando {self.carrera}")

# Uso de las clases
estudiante = Estudiante("Ana", 22, "Ingeniería")
estudiante.mostrar_info()
estudiante.estudiar()
