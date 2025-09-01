# Esta clase Diccionario representa un diccionario que podría verificar si una palabra es correcta.
# Está escrita de forma independiente, sin depender de implementaciones concretas de otras clases.
class Diccionario:
    def verificar_palabra(self, palabra):
        # Aquí iría la lógica para verificar palabras
        pass

# La clase CorrectorOrtografico usa un Diccionario para corregir textos.
# Según DIP, las clases de alto nivel (CorrectorOrtografico) no deben depender directamente
# de clases de bajo nivel (Diccionario) sino de abstracciones.
class CorrectorOrtografico:
    def __init__(self):
        # Aquí hay una dependencia directa (acoplamiento fuerte) a la clase Diccionario,
        # lo que NO cumple totalmente con DIP porque CorrectorOrtografico está atado a una implementación específica.
        self.diccionario = Diccionario()

    def corregir_texto(self, texto):
        # Usaríamos el diccionario para corregir el texto, delegando la verificación de palabras.
        pass

# Principio de Inversión de Dependencias (DIP) en palabras simples:
# Las clases deben depender de abstracciones (interfaces o clases abstractas), no de clases concretas.
# Esto permite cambiar implementaciones sin afectar a las clases que las usan,
# facilitando mantenimiento y extensión del código.
