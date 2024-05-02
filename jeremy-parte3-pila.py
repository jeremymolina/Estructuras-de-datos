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

# Clase pila
class Pila:
    def __init__(self):
        self.datos = []

    def add2Pila(self, persona):
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
            print(f"Persona {nombre} eliminada pila")
        else:
            print(f"Persona {nombre} no existe")

    def removefPila(self):
        if self.check_if_empty_pila():
            print("Pila vacia")
            return None
        else:
            return self.datos.pop()

    def check_if_empty_pila(self):
        return len(self.datos) == 0

personas = []
pila = Pila()
for _ in range(100):
    nombre = f"Persona {random.randint(1, 100)}"
    edad = random.randint(18, 80)
    direccion = f"Calle {random.randint(1, 100)}"
    persona = Persona(nombre, edad, direccion)
    personas.append(persona)
    pila.add2Pila(persona)

# Programa Pila
while True:
    print("\nMenu Pila:")
    print("1. Add persona")
    print("2. Remove persona")
    print("3. Print Pila")
    print("4. Remove Persona especifica Pila")
    print("4. Exit")

    op = int(input("Operacion: "))

    if op == 1:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        direccion = input("Dirección: ")
        persona = Persona(nombre, edad, direccion)
        pila.add2Pila(persona)
        print(f"Persona {persona.nombre} agregada a pila correctamente")
    elif op == 2:
        persona_removal = pila.removefPila()
        if persona_removal:
            print(f"Persona eliminada de pila: {persona_removal.nombre} - {persona_removal.edad} años - {persona_removal.direccion}")
        else:
            pass  # Checkpoint-exit si la pila esta vacia
    elif op == 3:
        print("Imprimiendo pila:")
        if pila.check_if_empty_pila():
            print("Pila vacia")
        else:
            for p in pila.datos:
                print(f"- {p.nombre} - {p.edad} años - {p.direccion}")
    elif op == 4:
        nombre = input("Nombre persona a remover: ")
        pila.remove_persona(nombre)
    elif op == 5:
        print("Exit...")
        break
    else:
        print("op invalida")
