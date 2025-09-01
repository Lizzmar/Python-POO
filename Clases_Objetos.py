# Definimos una CLASE llamada Celular. clase es como un "molde" o "plantilla" que nos permite crear OBJETOS.
# Los objetos son "cosas concretas" creadas a partir de ese molde.
class Celular:
    # Se ejecuta automáticamente cada vez que creamos un objeto de esta clase.
    # Sirve para inicializar los ATRIBUTOS del objeto.
    def __init__(self, marca, modelo, camara):
        # "self" representa al OBJETO que se está creando.
        # Gracias a self, cada objeto puede tener sus propios valores en sus atributos.
        self.marca = marca     
        self.modelo = modelo   
        self.camara = camara    

    # Este es un MÉTODO (función dentro de una clase).
    # Los métodos definen comportamientos que puede tener el objeto.
    def llamar(self):
        print("Esta haciendo un llamado")
        # Usamos f-string para acceder al atributo "modelo" del objeto con self.modelo
        print(f'Estás haciendo un llamado desde un: {self.modelo}')

    # Otro MÉTODO: cortar.
    def cortar(self):
        print("Cortaste la llamada")
    

# Ahora creamos OBJETOS a partir de la clase Celular.
# Cada objeto tiene sus propios ATRIBUTOS únicos.
celular1 = Celular("Readme", "5g Primer", "45 Mp")  
celular2 = Celular("Samsung", "Galaxy", "45 Mp")  

# Mostramos el atributo "modelo" del objeto celular1
print(celular1.modelo)  # Esto imprimirá: 5g Primer

# Llamamos al MÉTODO "llamar" en el objeto celular2
celular2.llamar()  # Imprime dos mensajes

# Llamamos al MÉTODO "cortar" en el objeto celular1
celular1.cortar()  # Imprime "Cortaste la llamada"
