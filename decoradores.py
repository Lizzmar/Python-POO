# Definición de un decorador simple
def mi_decorador(funcion):
    # Función interna que envuelve la función original
    def funcion_envoltura():
        print("Antes de llamar a la función")
        funcion()  # Ejecutar la función original
        print("Después de llamar a la función")
    # Retornamos la función envuelta que contiene la funcionalidad extra
    return funcion_envoltura

# Decoramos la función con el decorador usando la sintaxis @
@mi_decorador
def saludo():
    print("Hola, soy una función decorada")

# Llamamos a la función decorada
saludo()
