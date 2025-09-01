class HombreDeGalleta:
    def __init__(self, sabor, tamaño, decoracion):
        # __init__ = constructor → da los atributos iniciales a cada galleta
        self.sabor = sabor
        self.tamaño = tamaño
        self.decoracion = decoracion
    
    def saludar(self):
        print(f"Hola, soy un hombre de galleta {self.sabor} con {self.decoracion}")


galleta1 = HombreDeGalleta("chocolate", "grande", "chispas")
galleta2 = HombreDeGalleta("vainilla", "mediana", "glaseado")

print(galleta1.sabor)  # chocolate
print(galleta2.decoracion)  # glaseado

galleta1.saludar() 
galleta2.saludar()  


# El de la derecha (sabor) es el valor que llega desde afuera (temporal).
# El de la izquierda (self.sabor) es lo que se guarda en la galleta (permanente en ese objeto).