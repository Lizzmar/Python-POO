class Personaje:
    def __init__(self, nombre, nivel_poder):
        # Inicializamos el personaje con nombre y nivel de poder
        self.nombre = nombre
        self.nivel_poder = nivel_poder

    def __str__(self):
        # Representación legible del personaje
        return f"Personaje: {self.nombre} - Nivel de poder: {self.nivel_poder}"

    def __add__(self, otro):
        # Fusiona dos personajes, sumando sus niveles de poder y uniendo nombres
        nombre_fusion = f"{self.nombre} {otro.nombre}"
        poder_fusion = self.nivel_poder + otro.nivel_poder
        return Personaje(nombre_fusion, poder_fusion)

def crear_personaje():
    nombre = input("Introduce el nombre del personaje: ")
    nivel_poder = int(input("Introduce el nivel de poder: "))
    return Personaje(nombre, nivel_poder)

def mostrar_personajes(personajes):
    for i, p in enumerate(personajes, 1):
        print(f"{i}. {p}")

def main():
    personajes = []

    while True:
        print("\n1. Crear personaje")
        print("2. Mostrar personajes")
        print("3. Fusionar personajes")
        print("4. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            p = crear_personaje()
            personajes.append(p)
            print(f"Personaje {p.nombre} creado.")
        elif opcion == "2":
            if personajes:
                mostrar_personajes(personajes)
            else:
                print("No hay personajes creados.")
        elif opcion == "3":
            if len(personajes) < 2:
                print("Necesitas al menos dos personajes para fusionar.")
                continue
            mostrar_personajes(personajes)
            idx1 = int(input("Selecciona el número del primer personaje: ")) - 1
            idx2 = int(input("Selecciona el número del segundo personaje: ")) - 1
            if idx1 == idx2 or idx1 not in range(len(personajes)) or idx2 not in range(len(personajes)):
                print("Selección inválida.")
                continue
            fusion = personajes[idx1] + personajes[idx2]
            personajes.append(fusion)
            print(f"¡Nueva fusión creada! {fusion}")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    main()
