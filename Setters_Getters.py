class Persona:
    def __init__(self, nombre, edad):
        # Atributos privados con doble guion bajo para encapsulamiento real
        self.__nombre = nombre
        self.__edad = edad
    
    # Método getter para obtener el valor de nombre
    def get_nombre(self):
        return self.__nombre
    
    # Método setter para modificar el valor de nombre
    def set_nombre(self, nuevo_nombre):
        # Aquí podríamos agregar validaciones antes de asignar
        self.__nombre = nuevo_nombre

    # Método getter para obtener la edad
    def get_edad(self):
        return self.__edad

    # Método setter para modificar la edad
    def set_edad(self, nueva_edad):
        if nueva_edad > 0:
            self.__edad = nueva_edad
        else:
            print("Edad no válida")

# Crear instancia
persona = Persona("Jose", 21)

# Usar getters para obtener data encapsulada
print(persona.get_nombre())  
print(persona.get_edad())    

# Usar setters para modificar data encapsulada
persona.set_nombre("Maria")
persona.set_edad(30)

print(persona.get_nombre())  # Maria
print(persona.get_edad())    # 30

persona.set_edad(-5)  # Edad no válida (validación en setter)


# Getters son métodos usados para acceder o obtener el valor de un atributo privado. 
# Protegen el atributo permitiendo un acceso controlado.

# Setters son métodos usados para modificar o establecer el valor de un atributo privado, 
# idealmente con validaciones para mantener la integridad del dato.