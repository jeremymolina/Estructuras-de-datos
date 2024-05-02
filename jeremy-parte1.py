# Semana 3
import time # util para poder hacer la "tabla" de comparacion de los tiempos que nos toma ejecutar los algoritmos

# Func O(n)
def algoritmo_lineal(n):
    for i in range(n):
        # simple op
        pass

# Func O(n log n)
def algoritmo_logaritmico(n):
    for i in range(n):
        # log
        pass

# Func O(n^2)
def algoritmo_cuadratico(n):
    for i in range(n):
        for j in range(n):
            # cuadratica
            pass

# Tiempo de ejecucion por (n) entries
n_valores = [1000, 5000, 10000]

for n in n_valores:
    # Algoritmo lineal
    start_time = time.time()
    algoritmo_lineal(n)
    end_time = time.time()
    tiempo_lineal = end_time - start_time

    # Algoritmo log
    start_time = time.time()
    algoritmo_logaritmico(n)
    end_time = time.time()
    tiempo_logaritmico = end_time - start_time

    # Algoritmo cuadratico
    start_time = time.time()
    algoritmo_cuadratico(n)
    end_time = time.time()
    tiempo_cuadratico = end_time - start_time

    # R1 : Comparacion de tiempos de ejecucion
    print(f"n = {n}")
    print(f"Tiempo lineal: {tiempo_lineal:.3f} segundos")
    print(f"Tiempo logaritmico: {tiempo_logaritmico:.3f} segundos")
    print(f"Tiempo cuadratico: {tiempo_cuadratico:.3f} segundos")
    print("-" * 20)

    # R1 : O-grande nos dice como la cantidad de datos de entrada y el algoritmo aumentan el tiempo de ejecucion
    # de cada operacion, entre la lineal y el logaritmico la diferencia es minima, pero la cuadratica, cada iteracion
    # aumenta exponencialmente su tiempo de ejecucion.


    # R2 : ordenamiento de burbuja y ordenamiento de Mergesort
    # Burbuja: el algoritmo tiene que comparar todo con todos sus pares adyacentes, haciendo que entre mas (n) mas 
    # iteraciones deberan ser recorridas para poder resolver el ordenamiento, haciendo mas costoso en tiempo
    # y ciclos de memoria para poder ejecutar esta misma tarea. PD: No recuerdo si esto fue mencionado en el material 
    # pero en terminos generales uno quiere lograr el mismo resultado con menos ciclos de cpu para que este sea mas 
    # rapido y eficiente, esto hace que 
    # Mergesort: que divide y venceras, divide la lista en chunks mas pequenios de forma recursiva haciendo que la lista
    # se ordene mas rapido y con muchos menos ciclos de reloj
    