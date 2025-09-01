class MiClase:
    def __init__(self):
        # Atributo con un guion bajo: convención para indicar que es "protegido" o interno
        self._satributo_privado = "Valor"
    
    def _hablar(self):
        # Método con un guion bajo: también se indica que es un método interno o protegido
        print("Hola como estas")

# Crear instancia de la clase
objeto = MiClase()

# Se puede acceder al método, pero la convención sugiere no hacerlo directamente desde fuera
print(objeto._hablar())

#Encapsulamiento cuyo propósito es ocultar el estado interno de un objeto y protegerlo del
# acceso no autorizado o modificación directa desde fuera del objeto