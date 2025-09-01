# ==================================
# EJERCICIO 1.1 - Estudiante fijo
# ==================================
class Estudiante:
    def __init__(self, nombre, edad, grado):
        self.nombre = nombre
        self.edad = edad
        self.grado = grado

    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando en el grado {self.grado}.")


# Crear un objeto estudiante fijo
estudiante1 = Estudiante("Pedro", 23, 2)

print("===== Ejercicio 1.1 =====")
print(f"Nombre: {estudiante1.nombre}")
print(f"Edad: {estudiante1.edad}")
print(f"Grado: {estudiante1.grado}")
estudiante1.estudiar()  # ejecuta el método estudiar


# ==================================
# EJERCICIO 1.2 - Estudiante con input
# (escribe 'estudiar' para ejecutar el método)
# ==================================
class Student:
    def __init__(self, name, age, grade):
        # Guardamos todo en español para mantener consistencia
        self.nombre = name
        self.edad = age
        self.grado = grade

    def estudiar(self):
        print(f"El estudiante {self.nombre} está estudiando en el grado {self.grado}.")

    def mostrar_datos(self):
        print("\n===== Datos del estudiante =====")
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Grado: {self.grado}")


# Pedir datos al usuario
print("\n===== Ejercicio 1.2 =====")
nombre_input = input("Dime cuál es tu nombre: ").strip()
edad_input = input("Ahora dime tu edad: ").strip()
grado_input = input("Ahora dime tu grado: ").strip()

# Crear objeto con los datos ingresados
estudiante2 = Student(nombre_input, edad_input, grado_input)

# Mostrar datos
estudiante2.mostrar_datos()

# Permitir escribir 'estudiar' para ejecutar el método
accion = input("\nEscribe 'estudiar' para que el estudiante estudie ").strip().lower()
if accion == "estudiar":
    estudiante2.estudiar()
else:
    print("Listo. No se ejecutó el método 'estudiar'.")
