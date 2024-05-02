# En mi computadora siempre debo darle ejecutar dos veces a este ejercicio para que cargue.

# Semana 7 - 10
# Estas libs las aprendimos en cursos anteriores para el Proyecto final de Algebra
import os
from collections import defaultdict
import json
import networkx as nx
import matplotlib.pyplot as plt

# Leer dataset
prerequisites_file = os.path.join("parte4/ucsd-course-prerequisites/all_prerequisites.json")


# R4-3 : Este algortimo de ordenamiento topologico es base para el entendimiento de grafos
# Con el podemos ordenar y dar un sentido logico a tareas donde hay dependencias.
# por ejemplo el dataset que utilice es de cursos de la univeridad UCSD y contiene las
# dependencias entre los cursos entre si y de multiples carreras, aunque creo haber logrado 
# lo necesario para satisfacer la respuesta considero que hay muchas otras formas de haber sacado
# mayor provecho a este algoritmo y dataset, ver nota al final del archivo.

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topological_sort_util(self, v, visited, stack):
        visited[v] = True
        for i in self.graph[v]:
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        stack.append(v)

    def topological_sort(self):
        visited = [False] * (len(self.graph))
        stack = []
        for i in range(len(self.graph)):
            if not visited[i]:
                self.topological_sort_util(i, visited, stack)
        return stack[::-1]

# Construimos un grafo desde el archivo json
g = Graph()
with open(prerequisites_file, 'r') as file:
    data = json.load(file)
    for course in data:
        for prerequisite in data[course]:
            g.add_edge(prerequisite, course)

# ordenamos topologicamente
topological_order = g.topological_sort()
print("Orden topologico:", topological_order)

# Haciendo un poquito de extra graficar siempre es 
# visualmente mas facil de entender, asi que inclui 
# esta function con matplotlib y networkx
G = nx.DiGraph()
for i, course_code in enumerate(topological_order):
    G.add_node(course_code)
    prerequisites = topological_order[0:i]
    for prereq in prerequisites:
        G.add_edge(prereq, course_code)

# Visualizacion 
pos = nx.shell_layout(G)  # Debido ha que hay un orden jeraquico con las dependencias de cursos decidi esa este forma de anidar los nodos
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.title("Prerequisite de Cursos")
plt.show()


# Nota: No estoy satisfecho con este resultado, hubiera querido usar el dicccionario 
# del nombre de los cursos pero no recuerdo como hacerlo, buscando el como hacerlo tampoco
# logre dar con la logica que me funcionaria ademas de claro modificar el dataset
# original.