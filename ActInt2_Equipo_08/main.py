import numpy as np
from scipy.spatial import distance
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
        centrales = [tuple(map(int, archivo.readline().strip("()\n").split(","))) for _ in range(N)]

        # Leer las coordenadas de la nueva central
        nueva_central = tuple(map(int, archivo.readline().strip("()\n").split(",")))

        return N, matriz_distancias, matriz_flujos, centrales, nueva_central


# ======================================================================
# Función para aplicar el algoritmo de Floyd-Warshall
# Calcula las distancias mínimas entre todos los pares de nodos en un grafo.
# @param matriz_distancias: La matriz de distancias entre nodos.
# @return: Matriz con las distancias mínimas entre todos los pares de nodos.
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
# @param matriz_distancias:
# @return: 
# ======================================================================

# ======================================================================
# Paso 3
#
# @param matriz_distancias:
# @return: 
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
# @param nueva_central_idx: Índice del nodo de la nueva central.
# @return: Índice de la central más cercana y la distancia.
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
# @param nueva_central_idx: Índice del nodo de la nueva central.
# @return: Lista de distancias desde la nueva central a todas las centrales existentes.def encontrar_central_mas_cercana_con_dijkstra(matriz_distancias, nueva_central_idx):
# ======================================================================
def encontrar_central_mas_cercana_con_dijkstra(matriz_distancias, nueva_central_idx):
    distancias = dijkstra(matriz_distancias, nueva_central_idx)
    return distancias

# ======================================================================
# Función para ampliar el grafo con la nueva central (Paso 4)
# @param N: Número actual de nodos en el grafo.
# @param matriz_distancias: Matriz de distancias actual.
# @param centrales: Lista de coordenadas de las centrales existentes.
# @param nueva_central: Coordenadas de la nueva central.
# @return: Tupla con el nuevo número de nodos y la matriz de distancias ampliada.
# ======================================================================

def ampliar_grafo_con_nueva_central(N, matriz_distancias, centrales, nueva_central):
    N_ampliado = N + 1
    for i in range(len(centrales)):
        distancia_a_nueva_central = distance.euclidean(centrales[i], nueva_central)
        matriz_distancias[i].append(distancia_a_nueva_central)
    fila_nueva_central = [distance.euclidean(central, nueva_central) for central in centrales] + [0]
    matriz_distancias.append(fila_nueva_central)
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
        N, matriz_distancias, matriz_flujos, centrales, nueva_central = leer_datos_de_archivo(nombre_archivo_entrada)
        
        # Ampliar el grafo con la nueva central
        N_ampliado, matriz_distancias_ampliada = ampliar_grafo_con_nueva_central(N, matriz_distancias, centrales, nueva_central)

        # Índice de la nueva central
        nueva_central_idx = N_ampliado - 1

        # 1. Forma óptima de cablear las colonias con fibra (lista de arcos de la forma (A,B)).
        distancias_minimas = floyd_warshall(matriz_distancias)

        # 2. Ruta a seguir por el personal que reparte correspondencia (TSP)
        
        # 3. Valor de flujo máximo de información (Ford-Fulkerson o Edmonds-Karp)
        flujo_maximo = ford_fulkerson(matriz_flujos, 0, N-1)
        print(flujo_maximo)
        
        # 4. La central más cercana a la nueva contratación
        distancias = encontrar_central_mas_cercana_con_dijkstra(matriz_distancias_ampliada, nueva_central_idx)
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
            # archivo_salida.write("2. Ruta a seguir por el personal que reparte correspondencia:\n")
            # archivo_salida.write(str(ruta_correspondencia) + "\n\n")
            
            # 3. Valor del flujo máximo (cuando esté implementado)
            archivo_salida.write("3. Valor de flujo máximo de información:\n")
            archivo_salida.write(str(flujo_maximo) + "\n\n")
            
            # 4. 
            central_cercana_coordenadas = centrales[central_cercana_idx]
            nueva_central_coordenadas = nueva_central
            archivo_salida.write(f"4. La central más cercana a {nueva_central_coordenadas} es {central_cercana_coordenadas} con una distancia de {distancia_real:.3f} unidades.\n")

if __name__ == "__main__":
    main()
