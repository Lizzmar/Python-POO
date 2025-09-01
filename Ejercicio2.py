# Herencia Crear clases personas y estudiante
# La clase Persona tendra los atributos nombre y edad un metodo que imprima el nombre y la edad de la persona
# La clase Estudiante heredara de la clase Persona  y tendra un atributo adicional grado y un metodo que imprima el grado
# Debes de utilizar super en el metodo de inicializacion init para reutilizar clase padre Persona
# luego crear instancia Estudiante e imprime sus atributos y utiliza sus metodos para asegurarte de que todo funcione

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        
    def mostrar_datos(self):
        print(f"Nombre {self.nombre} Edad {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
        
    def mostrar_salario(self):
        print(f"Grado {self.grado}")

# Crear instancias de las clases
estudiante = Estudiante("Jose", 21, "8")

# Usar métodos
estudiante.mostrar_datos()