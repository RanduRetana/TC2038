import numpy as np
from scipy.spatial import distance
import heapq
maxsize = 9223372036854775807

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
        N = int(archivo.readline().strip())

        # Leer la matriz de distancias
        matriz_distancias = [list(map(int, archivo.readline().split())) for _ in range(N)]

        # Leer la matriz de flujos
        matriz_flujos = [list(map(int, archivo.readline().split())) for _ in range(N)]

        # Leer las coordenadas de las centrales
        centrales = [tuple(map(int, archivo.readline().strip("()\n").split(","))) for _ in range(N)]

        # Leer las coordenadas de la nueva central
        nuevo_punto = tuple(map(int, archivo.readline().strip("()\n").split(",")))

        return N, matriz_distancias, matriz_flujos, centrales, nuevo_punto


# ======================================================================
# Función para aplicar el algoritmo de Floyd-Warshall
# Calcula las distancias mínimas entre todos los pares de nodos en un grafo.
# @param matriz_distancias: La matriz de distancias entre nodos.
# @return: Matriz con las distancias mínimas entre todos los pares de nodos.
# complejidad: o(n^3)
# ======================================================================
def floyd_warshall(matriz_distancias):
    N = len(matriz_distancias)
    distancias_minimas = [[float('inf') for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if i == j:
                distancias_minimas[i][j] = 0
            elif matriz_distancias[i][j] != 0:
                distancias_minimas[i][j] = matriz_distancias[i][j]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if distancias_minimas[i][k] + distancias_minimas[k][j] < distancias_minimas[i][j]:
                    distancias_minimas[i][j] = distancias_minimas[i][k] + distancias_minimas[k][j]

    return distancias_minimas


# ======================================================================
# Paso 2
#
# Función Traveling Salesman Problem (TSP)
#
# Consiste en encontrar el camino más corto que recorre n ciudades
# o puntos de interés y vuelve al punto de partida, pasando por cada ciudad
# exactamente una vez.
#
# @param matriz_distancias, la matriz de distancias entre nodos.
# @param nodo_inicial, indica el nodo inicial para el recorrido.
# @param numNodos, número de nodos del grafo.
# @return lista_recorrido_minimo (int), regresa lista del recorrido óptimo.
# @return peso_minimo(int), regresa el costo mas bajo.
# Complejidad: O(n!), donde "n" es la cantidad de vértives en el grafo.
# ======================================================================
def Tsp(matriz_distancias, nodo_inicial, num_nodos):
    def generar_permutaciones(nodos):
        if not nodos:
            return [[]]
        return [[nodo] + p for i, nodo in enumerate(nodos) for p in generar_permutaciones(nodos[:i] + nodos[i+1:])]

    vertices = list(range(num_nodos))
    vertices.remove(nodo_inicial)

    peso_minimo = maxsize
    lista_ordenada = None

    for perm in generar_permutaciones(vertices):
        peso_actual = 0
        k = nodo_inicial
        orden_recorrido = [k] + perm
        for j in perm:
            peso_actual += matriz_distancias[k][j]
            k = j
        peso_actual += matriz_distancias[k][nodo_inicial]
        orden_recorrido.append(nodo_inicial)

        if peso_actual < peso_minimo:
            peso_minimo = peso_actual
            lista_ordenada = orden_recorrido

    return lista_ordenada, peso_minimo

# Paso 3
#
# @param matriz_flujos: La matriz de flujos entre nodos.
# @param nodo_inicial: El nodo inicial del camino de aumento.
# @param nodo_final: El nodo final del camino de aumento.
# @return: El flujo máximo de información que se puede enviar desde el nodo inicial al nodo final.
# complejidad: O(V * E^2)
# ======================================================================
# Función ford_fulkerson actualizada
def ford_fulkerson(matriz_flujos, nodo_inicial, nodo_final):
    N = len(matriz_flujos)
    matriz_flujos_residuales = [list(row) for row in matriz_flujos]
    flujo_maximo = 0

    while True:
        padres = bfs(matriz_flujos_residuales, nodo_inicial, nodo_final)
        if padres is None:  # No hay más caminos de aumento
            break

        # Encontrar el flujo mínimo en el camino encontrado
        flujo_camino = float('inf')
        v = nodo_final
        while v != nodo_inicial:
            u = padres[v]
            flujo_camino = min(flujo_camino, matriz_flujos_residuales[u][v])
            v = u

        # Actualizar el flujo máximo y el grafo residual
        flujo_maximo += flujo_camino
        v = nodo_final
        while v != nodo_inicial:
            u = padres[v]
            matriz_flujos_residuales[u][v] -= flujo_camino
            matriz_flujos_residuales[v][u] += flujo_camino
            v = u

    return flujo_maximo

# Función bfs actualizada
# ======================================================================
# @param matriz_flujos_residuales: La matriz de flujos residuales entre nodos.
# @param nodo_inicial: El nodo inicial del camino de aumento.
# @param nodo_final: El nodo final del camino de aumento.
# @return: Lista de padres de cada nodo en el camino de aumento.
# complejidad: O(V * E)
# ======================================================================
def bfs(matriz_flujos_residuales, nodo_inicial, nodo_final):
    N = len(matriz_flujos_residuales)
    visitados = [False] * N
    cola = [nodo_inicial]
    visitados[nodo_inicial] = True
    padres = [-1] * N

    while cola:
        u = cola.pop(0)
        for v, capacidad in enumerate(matriz_flujos_residuales[u]):
            if capacidad > 0 and not visitados[v]:
                cola.append(v)
                padres[v] = u
                visitados[v] = True
                if v == nodo_final:
                    return padres
    return None

# ======================================================================
# Paso 4
# Función para encontrar la central más cercana utilizando Dijkstra para el camino más corto.
# @param matriz_distancias: La matriz de distancias entre nodos.
# @param nuevo_punto_idx: Índice del nodo de la nueva central.
# @return: Índice de la central más cercana y la distancia.
# complejidad: O(V log V + E log V)
# ======================================================================
def dijkstra(matriz_distancias, nodo_inicio):
    N = len(matriz_distancias)
    distancias = [float('inf')] * N
    distancias[nodo_inicio] = 0
    cola_prioridad = [(0, nodo_inicio)]

    while cola_prioridad:
        distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)
        if distancia_actual > distancias[nodo_actual]:
            continue

        for vecino, peso in enumerate(matriz_distancias[nodo_actual]):
            if peso > 0:
                distancia = distancia_actual + peso
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))

    return distancias

# ======================================================================
# Función para encontrar la central más cercana utilizando Dijkstra
# @param matriz_distancias: La matriz de distancias entre nodos.
# @param nuevo_punto_idx: Índice del nodo de la nueva central.
# @return: Lista de distancias desde la nueva central a todas las centrales existentes.def encontrar_central_mas_cercana_con_dijkstra(matriz_distancias, nuevo_punto_idx):
# ======================================================================
def encontrar_central_mas_cercana_con_dijkstra(matriz_distancias, nuevo_punto_idx):
    distancias = dijkstra(matriz_distancias, nuevo_punto_idx)
    return distancias

# ======================================================================
# Función para ampliar el grafo con la nueva central (Paso 4)
# @param N: Número actual de nodos en el grafo.
# @param matriz_distancias: Matriz de distancias actual.
# @param centrales: Lista de coordenadas de las centrales existentes.
# @param nuevo_punto: Coordenadas de la nueva central.
# @return: Tupla con el nuevo número de nodos y la matriz de distancias ampliada.
# ======================================================================

def ampliar_grafo_con_nuevo_punto(N, matriz_distancias, centrales, nuevo_punto):
    N_ampliado = N + 1
    for i in range(len(centrales)):
        distancia_a_nuevo_punto = distance.euclidean(centrales[i], nuevo_punto)
        matriz_distancias[i].append(distancia_a_nuevo_punto)
    fila_nuevo_punto = [distance.euclidean(central, nuevo_punto) for central in centrales] + [0]
    matriz_distancias.append(fila_nuevo_punto)
    return N_ampliado, matriz_distancias


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
        N, matriz_distancias, matriz_flujos, centrales, nuevo_punto = leer_datos_de_archivo(nombre_archivo_entrada)
        
        # Ampliar el grafo con la nueva central
        N_ampliado, matriz_distancias_ampliada = ampliar_grafo_con_nuevo_punto(N, matriz_distancias, centrales, nuevo_punto)

        # Índice de la nueva central
        nuevo_punto_idx = N_ampliado - 1

        # 1. Forma óptima de cablear las colonias con fibra (lista de arcos de la forma (A,B)).
        distancias_minimas = floyd_warshall(matriz_distancias)

        # 2. Ruta a seguir por el personal que reparte correspondencia (TSP)
        # Nodo inicial para recorrido
        nodo_inicial = 0
        resultado, peso = Tsp(matriz_distancias, nodo_inicial, N)
        
        # 3. Valor de flujo máximo de información (Ford-Fulkerson o Edmonds-Karp)
        flujo_maximo = ford_fulkerson(matriz_flujos, 0, N-1)

        # 4. La central más cercana a la nueva contratación
        distancias = encontrar_central_mas_cercana_con_dijkstra(matriz_distancias_ampliada, nuevo_punto_idx)
        central_cercana_idx = np.argmin(distancias[:-1])
        distancia_real = distancias[central_cercana_idx]
        
        # Crear el nombre del archivo de salida basado en el archivo de entrada
        nombre_archivo_salida = nombre_archivo_entrada.replace('Entrada', 'Salida')
        
        # Escribir los resultados en el archivo de salida
        with open(nombre_archivo_salida, 'w') as archivo_salida:


            # 1.
            archivo_salida.write("1. Todas las conexiones posibles entre colonias con sus respectivas distancias mínimas:\n")
            for i in range(N):
                for j in range(N):
                    if i != j:
                        distancia = distancias_minimas[i][j]
                        archivo_salida.write(f"Colonia {i+1} a colonia {j+1}: {distancia}\n")
                archivo_salida.write("\n")

            # 2. Ruta de correspondencia (cuando esté implementada)
            archivo_salida.write("2. Ruta a seguir por el personal que reparte correspondencia:\n")
            archivo_salida.write(f"Ruta óptima: {resultado}. Peso del recorrido mas corto: {peso}\n\n")

            archivo_salida.write(str() + "\n\n")
            
            # 3. Valor del flujo máximo (cuando esté implementado)
            archivo_salida.write("3. Valor de flujo máximo de información:\n")
            archivo_salida.write(str(flujo_maximo) + "\n\n")
            
            # 4. 
            central_cercana_coordenadas = centrales[central_cercana_idx]
            nuevo_punto_coordenadas = nuevo_punto
            archivo_salida.write(f"4. La central más cercana a {nuevo_punto_coordenadas} es {central_cercana_coordenadas} con una distancia de {distancia_real:.3f} unidades.\n")

if __name__ == "__main__":
    main()