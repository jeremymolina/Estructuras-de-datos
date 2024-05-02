# ------------- R 4.1 #
num_nodes = 6

print("\nNODOS DIRIGIDOS CONETADOS:")
# Inicializamos matriz
adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

# grafo dirigido completamente conectado
for i in range(num_nodes):
    for j in range(num_nodes):
        if i != j:
            adj_matrix[i][j] = 1

# Imprimir representacion
print("Como tabla:")
print("   ", end="")
for i in range(num_nodes):
    print(f" {i} ", end="")
print()
for i in range(num_nodes):
    print(f"{i} |", end="")
    for j in range(num_nodes):
        print(f" {adj_matrix[i][j]} ", end="")
    print()

# Representacion de ligue entre nodos:
print("\nLigue entre nodos:")
for i in range(num_nodes):
    for j in range(num_nodes):
        if adj_matrix[i][j] == 1:
            print(f"{i} -> {j}")


# ------------- R 4.2 #
# Nodos desconectados
print("\nNODOS NO DIRIGIDOS DESCONETADOS:")

# reiniciamos matriz
adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

# grafo no dirigido desconectado
for i in range(3):
    for j in range(3):
        if i != j:
            adj_matrix[i][j] = 1

for i in range(3, num_nodes):
    for j in range(3, num_nodes):
        if i != j:
            adj_matrix[i][j] = 1

# Imprimir representacion
print("\nComo tabla:")
print("   ", end="")
for i in range(num_nodes):
    print(f" {i} ", end="")
print()
for i in range(num_nodes):
    print(f"{i} |", end="")
    for j in range(num_nodes):
        print(f" {adj_matrix[i][j]} ", end="")
    print()


# Representacion de ligue entre nodos:
print("\nLigue entre nodos:")
for i in range(num_nodes):
    for j in range(num_nodes):
        if adj_matrix[i][j] == 1:
            print(f"{i} - {j}")
