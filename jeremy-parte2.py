# Semana 4
# R1
import random # libreria para generar data random para un poc


# definimos clase persona con sus 3 valores, nombre, edad, direccion
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

def bubble_sort(personas):
    n = len(personas)
    for i in range(n):
        for j in range(n - i - 1):
            if personas[j] > personas[j + 1]:
                personas[j], personas[j + 1] = personas[j + 1], personas[j]

# generamos randomized data
personas = []
for _ in range(100):
    nombre = f"Persona {random.randint(1, 100)}"
    edad = random.randint(18, 80)
    direccion = f"Calle {random.randint(1, 100)}"
    personas.append(Persona(nombre, edad, direccion))

# call bubble sort 
bubble_sort(personas)

# order lista e imprimirla
print("Lista de personas ordenada por edad:")
for persona in personas:
    print(f"{persona.nombre} - {persona.edad} años - {persona.direccion}")

# R1-a : Sobreescritura de __ eq__, __lt__ y __gt__
# Si no sobreescribieramos los datos bubble_sort no podria ordenarlos / "cambiar" el orden de los datos
# lo cual no nos permitiria orderlos por, en este caso, la edad.

# ------------------------ #

# R2
def busqueda_binaria(personas, age_lookup):
    compare_left_val = 0
    compare_right_val = len(personas) - 1

    while compare_left_val <= compare_right_val:
        halfen = (compare_left_val + compare_right_val) // 2 # me gusto usar el nombre halfen y halfanizer ya que en mi mente me da una idea inmediata de que hace
        persona_halftenizer = personas[halfen]

        if persona_halftenizer.edad == age_lookup:
            print(f"Persona encontrada: {persona_halftenizer.nombre} - {persona_halftenizer.edad} años - {persona_halftenizer.direccion}") # mas interesante dar el resultado de la busqueda, pero seria mas interesante decir si hay mas de uno, pero no hare esto para no complicar mucho la respuesta
            return True
        elif persona_halftenizer.edad < age_lookup:
            compare_left_val = halfen + 1
        else:
            compare_right_val = halfen - 1

    print(f"Persona no encontrada con edad {age_lookup}")
    return False

# Busqueda y resultado
age_lookup = int(input("Ingrese la edad a buscar: "))
busqueda_binaria(personas, age_lookup)
