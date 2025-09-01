from abc import ABC, abstractmethod

# Clase abstracta Trabajador solo con el método trabajar,
# define un contrato para clases que deben realizar trabajo
class Trabajador(ABC):
    @abstractmethod
    def trabajar(self):
        pass

# Clase abstracta Comedor con el método comer,
# para clases que tengan comportamiento de comer
class Comedor(ABC):
    @abstractmethod
    def comer(self):
        pass

# Clase abstracta Durmiente con el método dormir,
# que deben implementar las clases que puedan dormir
class Durmiente(ABC):
    @abstractmethod
    def dormir(self):
        pass


# La clase Humano implementa las tres interfaces:
# puede trabajar, comer y dormir
class Humano(Trabajador, Durmiente, Comedor):
    def comer(self):
        print("El humano esta comiendo")

    def trabajar(self):
        print("El humano esta trabajando")

    def dormir(self):
        print("El humano esta durmiendo")

# La clase Robot solo implementa Trabajador,
# porque sólo puede trabajar, no puede comer ni dormir
class Robot(Trabajador):
    def trabajar(self):
        print("El robot esta trabajando")


# Crear instancias
robot = Robot()
humano = Humano()

# Usar métodos
robot.trabajar()  # Funciona porque Robot tiene trabajar
humano.trabajar() # Funciona para humano también
humano.comer()    # Humano come, pero Robot no, lo cual es correcto


# El Principio de Segregación de Interfaces (ISP) = clase no debe verse obligada a depender de métodos que no usa. 
# las interfaces deben ser pequeñas y específicas para que las clases implementen solo lo que realmente necesitan. 
#Evitar que una clase tenga que implementar funciones innecesarias, hace el código más limpio, fácil de mantener.