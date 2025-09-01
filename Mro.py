# MRO = Method Resolution Order (Orden de resolución de métodos)
# En este ejemplo, la jerarquía queda así:
# D → B → A → C → F → object
# (el orden real lo determina Python internamente con el algoritmo C3)

class A:
    def hablar(self):
        print("Hola desde A")

class F:
    def hablar(self):
        print("Hola desde F")

class B(A):  # B hereda de A
    def hablar(self):
        print("Hola desde B")
        
class C(F):  # C hereda de F
    def hablar(self):
        print("Hola desde C")
        
class D(B, C):  # D hereda de B y C (herencia múltiple)
    def hablar(self):
        print("Hola desde D")

# Creamos un objeto de tipo D
d = D()

# Llamamos explícitamente al método 'hablar' de la clase F
F.hablar(d)
