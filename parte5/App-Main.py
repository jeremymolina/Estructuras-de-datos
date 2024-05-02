from AVLTree import AVLTree
from Persona import Persona
import random

root = None
avl_tree = AVLTree()

# Inicializar Tree con some random data como el ejercicio #2 con la diferencia que aca en una funcion asi es mas "app-alike"
def generate_random_data():
    personas = []
    names = ["Juan", "Maria", "Carlos", "Ana", "Pedro", "Laura", "Luis", "Sofia"]
    for _ in range(10):
        nombre = random.choice(names)
        edad = random.randint(18, 80)
        direccion = f"Calle {random.randint(1, 100)}"
        personas.append(Persona(nombre, edad, direccion))
    return personas

# Agregar persona al tree
def add_person():
    global root
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    direccion = input("Direccion: ")
    persona = Persona(nombre, edad, direccion)
    root = avl_tree.insert_node(root, persona)
    print("Persona agregada!")

# Eliminar persona del tree
def remove_person():
    global root
    if root:
        nombre = input("Nombre de la persona: ")
        edad = int(input("Edad de la persona: "))
        if avl_tree.search(root, nombre, edad):  
            persona = Persona(nombre, edad, "")
            root = avl_tree.delete_node(root, persona)
            print("Persona eliminada!!!")
        else:
            print("No se encuentra a la persona con ese nombre y edad.")
    else:
        print("Tree vacio, no se puede eliminar datos")

def print_tree():
    if root:
        print("\nAVL Tree:")
        avl_tree.print_tree(root)
    else:
        print("Tree vacio")

# Generate random data and insert into AVL tree
random_personas = generate_random_data()
for persona in random_personas:
    root = avl_tree.insert_node(root, persona)

while True:
    print("\n1. Add Persona")
    print("2. Remove Persona")
    print("3. Print Tree")
    print("4. Exit")

    op = input("Opcion: ")

    if op == '1':
        add_person()
    elif op == '2':
        remove_person()
    elif op == '3':
        print_tree()
    elif op == '4':
        print("Exit...")
        break
    else:
        print("Opcion Invalida")
