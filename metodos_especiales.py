class Persona:
    def __init__(self, nombre, edad):
        # Método constructor: se ejecuta al crear el objeto
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        # Método especial que devuelve una representación legible al imprimir el objeto
        return f"Nombre: {self.nombre}, Edad: {self.edad}"

    def __eq__(self, otro):
        # Método especial para comparar dos objetos de esta clase
        # Retorna True si tienen mismo nombre y edad
        if isinstance(otro, Persona):
            return self.nombre == otro.nombre and self.edad == otro.edad
        return False

# Crear instancias
persona1 = Persona("Jose Andres", 21)
persona2 = Persona("Carlos", 30)
persona3 = Persona("Juan Carlos", 30)

# Uso de __str__
print(persona1)  

# Comparar objetos con __eq__
print(persona1 == persona2)  # False porque nombres diferentes
print(persona1 == persona3)  # True porque nombres y edad iguales
