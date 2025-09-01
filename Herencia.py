class Persona:
    def __init__(self,nombre,edad,nacionalidad):
        self.nombre=nombre 
        self.edad=edad
        self.nacionalidad=nacionalidad
    
    def hablar(self):
        print("Hola")
        

class Empleado(Persona):
    def __init__(self, nombre, edad, nacionalidad,trabajo,salario):
        super().__init__(nombre, edad, nacionalidad)
        self.trabajo= trabajo
        self.salario= salario


# Herencia Jerárquica
class Estudiante(Persona):
    def __init__(self, nombre, edad, nacionalidad,notas,universidad):
        super().__init__(nombre, edad, nacionalidad)
        self.notas= notas
        self.universidad= universidad


# Herencia Múltiple
class Artista:
    def __init__(self,habilidad):
        self.habilidad=habilidad
    
    def mostrar_habilidad(self):
        print(f"Mi habilidad es {self.habilidad}")
        

class EmpleadoArtista(Persona,Artista):
    def __init__(self, nombre, edad, nacionalidad,habilidad,salario,empresa):
        Persona.__init__(self,nombre, edad, nacionalidad)
        Artista.__init__(self,habilidad)
        self.salario=salario
        self.empresa=empresa

    def presentarse(self):
        print(f"Hola, soy {self.nombre}, trabajo en {self.empresa} y:")
        super().mostrar_habilidad()   # llamamos a mostrar_habilidad de Artista
        

# Creamos un EmpleadoArtista
jose = EmpleadoArtista("Jose Andres",21,"Boliviano","Cantar",10000,"Google")

jose.hablar()           # método de Persona
jose.mostrar_habilidad()# método de Artista
jose.presentarse()      # método propio

herencia= issubclass(EmpleadoArtista,Persona)
print(herencia)

instancia= isinstance(jose,EmpleadoArtista)
print(instancia)