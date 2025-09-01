'''
class Ave:
    def volar(self):
        return "Estoy volando"
class Pinguino(Ave):
    def volar(self):
        return "No puedo volar"
def hacer_volar(ave= Ave):
    return ave.volar()
print(hacer_volar(Pinguino()))
'''

# El Principio (LSP) una clase hija debe poder reemplazar a su clase padre sin que el programa deje de funcionar correctamente. 
# si una función trabaja con objetos de la clase padre, también debe funcionar bien con objetos de la clase hija.
class Ave:
    pass
class AveVoladora(Ave):
    def volar(delf):
        return"Estoy volando"
class AveNoVoladora(Ave):
    pass