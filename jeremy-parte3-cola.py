# En mi computadora siempre debo darle ejecutar dos veces a este ejercicio para que cargue.

# Semana 5 - 6
# R1 -  mantenemos mismo codigo de parte2 segun instrucciones
import random

class Persona:
    def __init__(self, nombre, edad, direccion):
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion

    def __eq__(self, other):
        return self.edad == other.edad

    def __lt__(self, other):
        return self.edad < other.edad

    def __gt__(self, other):
        return self.edad > other.edad
    
# Clase cola
class Cola:
    def __init__(self):
        self.datos = []

    def add2Cola(self, persona):
        self.datos.append(persona)

    def search_persona(self, nombre):
        for i, p in enumerate(self.datos):
            if p.nombre == nombre:
                return i 
        return None  # Persona no encontrada

    def remove_persona(self, nombre):
        indice = self.search_persona(nombre)
        if indice is not None:
            del self.datos[indice]
            print(f"Persona {nombre} eliminada cola")
        else:
            print(f"Persona {nombre} no existe")

    def removefCola(self):
        if self.check_if_empty_cola():
            print("Cola vacia")
            return None
        else:
            return self.datos.pop(0)

    def check_if_empty_cola(self):
        return len(self.datos) == 0

# Generar datos aleatorios y agregar a la cola
personas = []
cola = Cola()
for _ in range(100):
    nombre = f"Persona {random.randint(1, 100)}"
    edad = random.randint(18, 80)
    direccion = f"Calle {random.randint(1, 100)}"
    persona = Persona(nombre, edad, direccion)
    personas.append(persona)
    cola.add2Cola(persona)

while True:
    print("\nMenú de Cola:")
    print("1. Add persona")
    print("2. Remove from cola")
    print("3. Print Cola")
    print("4. Remove Persona especifica Cola")
    print("4. Exit")

    op = int(input("Operacion: "))

    if op == 1:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        direccion = input("Dirección: ")
        persona = Persona(nombre, edad, direccion)
        cola.add2Cola(persona)
        print(f"Persona {persona.nombre} agregada a cola correctamente")
    elif op == 2:
        persona_removal = cola.removefCola()
        if persona_removal:
            print(f"Persona eliminada de cola: {persona_removal.nombre} - {persona_removal.edad} años - {persona_removal.direccion}")
        else:
            pass  # No se hace nada si la cola está vacía
    elif op == 3:
        print("Imprimiendo cola:")
        if cola.check_if_empty_cola():
            print("Cola vacia")
        else:
            for p in cola.datos:
                print(f"- {p.nombre} - {p.edad} años - {p.direccion}")
    elif op == 4:
        nombre = input("Nombre persona a remover: ")
        cola.remove_persona(nombre)
    elif op == 5:
        print("Exit...")
        break
    else:
        print("op invalida")
