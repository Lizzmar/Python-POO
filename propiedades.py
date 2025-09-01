#decorador en Python función que recibe otra función y devuelve una función nueva con funcionalidad adicional,

# El decorador @property convierte un método en una propiedad, permitiendo acceder a él como si fuera un atributo

class Persona:
    def __init__(self, nombre, edad):
        # Atributo privado con doble guion bajo para ocultar acceso directo
        self.__nombre = nombre
        # Atributo protegido con un solo guion bajo (convensión)
        self._edad = edad

    @property
    def nombre(self):
        # Getter: método que se comporta como atributo para obtener __nombre
        print("Getter llamado")
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        # Setter: método que se usa para asignar valor a __nombre con validación
        print("Setter llamado")
        if isinstance(nuevo_nombre, str) and nuevo_nombre != "":
            self.__nombre = nuevo_nombre
        else:
            print("Nombre inválido")

    @nombre.deleter
    def nombre(self):
        # Deleter: método que se usa para eliminar el atributo __nombre de forma controlada
        print("Deleter llamado")
        del self.__nombre

# Crear instancia
persona = Persona("Jose", 21)

# Acceder al atributo (invoca getter)
print(persona.nombre)

# Modificar el atributo (invoca setter)
persona.nombre = "Andres"
print(persona.nombre)

# Eliminar el atributo (invoca deleter)
del persona.nombre

# Intentar acceder al atributo después de eliminar (genera error)
# print(persona.nombre)  # Esto lanzaría un AttributeError
