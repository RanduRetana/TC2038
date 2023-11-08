import numpy as np
from scipy.spatial import distance
from itertools import permutations
import heapq

# ========================== FUNCIONES AUXILIARES ==========================

# ======================================================================
# Paso 1:  Leer un archivo de entrada que contiene la información de un grafo representado en forma
#  de una matriz de adyacencias con grafos ponderados.

# Función para leer los datos de entrada de un archivo
# @param nombre_archivo: Nombre del archivo de entrada.
# @return: Tupla con los datos de las matrices y la información de las centrales.
# ======================================================================
def leer_datos_de_archivo(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        # Leer el número de nodos
        N = int(archivo.readline().strip())

        # Leer la matriz de distancias
        matriz_distancias = [list(map(int, archivo.readline().split())) for _ in range(N)]

        # Leer la matriz de flujos
        matriz_flujos = [list(map(int, archivo.readline().split())) for _ in range(N)]

        # Leer las coordenadas de las centrales
        centrales = [tuple(map(int, archivo.readline().split())) for _ in range(N)]

        # Leer las coordenadas de la nueva central
        nueva_central = tuple(map(int, archivo.readline().split()))

        return N, matriz_distancias, matriz_flujos, centrales, nueva_central

# ======================================================================
# Paso 1.2: El programa debe desplegar cuál es la forma óptima de cablear con fibra óptica conectando 
# colonias de tal forma que se pueda compartir información entre cualesquiera dos colonias.

# Función para calcular el MST (árbol de mínima extensión) usando el algoritmo de Prim
# @param matriz_distancias: La matriz de distancias entre nodos.
# @param N: Número de nodos.
# @return: Lista de aristas que forman el árbol de expansión mínimo.
# ======================================================================
def prim(matriz_distancias, N):
    # Inicialización
    seleccionados = [0] * N
    no_of_edges = 0
    seleccionados[0] = True
    cableado = []

    # Número de aristas en MST  (árbol de mínima extensión) será N - 1
    while (no_of_edges < N - 1):
        minimo = float('inf')
        a = 0
        b = 0
        for m in range(N):
            if seleccionados[m]:
                for n in range(N):
                    if ((not seleccionados[n]) and matriz_distancias[m][n]):  
                        # no seleccionado y hay una arista
                        if minimo > matriz_distancias[m][n]:
                            minimo = matriz_distancias[m][n]
                            a = m
                            b = n
        cableado.append((chr(65 + a), chr(65 + b)))
        seleccionados[b] = True
        no_of_edges += 1
    
    return cableado

# ======================================================================
# Paso 2
#
# @param matriz_distancias:
# @return: 
# ======================================================================

# ======================================================================
# Paso 3
#
# @param matriz_distancias:
# @return: 
# ======================================================================

# ======================================================================
# Paso 4
# Función para encontrar la central más cercana utilizando Dijkstra para el camino más corto.
# @param matriz_distancias: La matriz de distancias entre nodos.
# @param nueva_central_idx: Índice del nodo de la nueva central.
# @return: Índice de la central más cercana y la distancia.
# ======================================================================
def encontrar_central_mas_cercana(matriz_distancias, nueva_central_idx):
    N = len(matriz_distancias)
    distancias = [float('inf')] * N
    distancias[nueva_central_idx] = 0
    pq = [(0, nueva_central_idx)]  # Cola de prioridad para seleccionar el siguiente nodo más cercano

    while pq:
        distancia_actual, nodo_actual = heapq.heappop(pq)
        if distancia_actual > distancias[nodo_actual]:
            continue
        for vecino in range(N):
            if matriz_distancias[nodo_actual][vecino] > 0:  # Asegurar que haya una conexión
                distancia = distancia_actual + matriz_distancias[nodo_actual][vecino]
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(pq, (distancia, vecino))

    central_cercana = min((index for index in range(N) if index != nueva_central_idx), key=lambda x: distancias[x])
    return central_cercana, distancias[central_cercana]

# ========================== FUNCIÓN PRINCIPAL ==========================

# ======================================================================
# Función principal que ejecuta el programa
# ======================================================================

def main():
    # Lista de archivos de entrada
    archivos_entrada = [
        'Equipo_08_Entrada_1.txt',
        'Equipo_08_Entrada_2.txt',
        'Equipo_08_Entrada_3.txt'
    ]

    for nombre_archivo_entrada in archivos_entrada:
        # Leer los datos de entrada
        N, matriz_distancias, matriz_flujos, centrales, nueva_central = leer_datos_de_archivo(nombre_archivo_entrada)

        # Obtener el índice de la nueva central basado en las coordenadas con cálculo euclidiano
        distancias_a_nueva_central = [distance.euclidean(central, nueva_central) for central in centrales]
        nueva_central_idx = np.argmin(distancias_a_nueva_central)
        
        # 1. Forma óptima de cablear las colonias con fibra (lista de arcos de la forma (A,B)).
        cableado = prim(matriz_distancias, N)
        
        # 2. Ruta a seguir por el personal que reparte correspondencia (TSP)
        
        # 3. Valor de flujo máximo de información (Ford-Fulkerson o Edmonds-Karp)
        
        # 4. La central más cercana a la nueva contratación
        central_cercana, distancia = encontrar_central_mas_cercana(matriz_distancias, nueva_central_idx)
        
        # Crear el nombre del archivo de salida basado en el archivo de entrada
        nombre_archivo_salida = nombre_archivo_entrada.replace('Entrada', 'Salida')
        
        # Escribir los resultados en el archivo de salida
        with open(nombre_archivo_salida, 'w') as archivo_salida:
            archivo_salida.write("1. Forma óptima de cablear las colonias con fibra:\n")
            archivo_salida.write(str(cableado) + "\n\n")
            
            # 2. Ruta de correspondencia (cuando esté implementada)
            # archivo_salida.write("2. Ruta a seguir por el personal que reparte correspondencia:\n")
            # archivo_salida.write(str(ruta_correspondencia) + "\n\n")
            
            # 3. Valor del flujo máximo (cuando esté implementado)
            # archivo_salida.write("3. Valor de flujo máximo de información:\n")
            # archivo_salida.write(str(valor_flujo_maximo) + "\n\n")
            
            archivo_salida.write(f"4. La central más cercana a la nueva contratación está en {chr(65 + central_cercana)} con una distancia de {distancia:.2f} unidades.\n")

# Ejecutar el programa principal
if __name__ == "__main__":
    main()
