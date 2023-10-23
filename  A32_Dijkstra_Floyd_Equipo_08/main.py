#======================================================================
# Actividad: Actividad 3.2b Implementación de "Dijkstra and Floyd"
# 
# Fecha: 21/10/2023
#
# Autores:
# Frida Bailleres González  | A01708633
# Marco Randu Retana Vargas | A01709521
# Sebastian Flores Lemus    | A01709229
#
# Descripción:
# En este programa se implementan los algoritmos de Dijkstra y Floyd para encontrar
# la distancia más corta entre parejas de nodos en un grafo dirigido. El grafo
# es representado mediante una matriz de adyacencia. El algoritmo de Dijkstra
# encuentra el camino más corto desde un nodo origen a todos los demás nodos, mientras
# que el algoritmo de Floyd-Warshall encuentra la distancia más corta entre cada
# par de nodos en el grafo.
#
# ======================================================================

# ======================================================================
# Función que implementa el algoritmo de Dijkstra
# @param graph: Matriz de adyacencia del grafo.
# @param src: Nodo fuente.
# @return: Lista de distancias más cortas desde el nodo fuente a todos los demás nodos.
# ======================================================================

def dijkstra(graph, src):
    # Número de nodos en el grafo.
    n = len(graph)
    
    # Inicializa todas las distancias como infinito y la distancia del nodo origen como 0.
    dist = [float("inf")] * n
    dist[src] = 0
    
    # Lista para mantener el registro de los nodos visitados.
    visited = [False] * n

    # Itera para todos los nodos.
    for _ in range(n):
        
        # Encuentra el nodo de distancia mínima de los nodos no procesados. 
        # u siempre será igual a src en la primera iteración.
        u = min_distance_node(dist, visited)
        
        # Marca el nodo de distancia mínima como visitado.
        visited[u] = True

        # Actualiza la distancia del nodo adyacente del nodo seleccionado.
        for v in range(n):
            
            # Actualiza dist[v] solo si no está en visited, hay un arco de u a v,
            # y el peso total del camino desde src a v a través de u es más pequeño que el valor actual de dist[v].
            if not visited[v] and graph[u][v] != -1 and dist[u] + graph[u][v] < dist[v]:
                dist[v] = dist[u] + graph[u][v]

    return dist

# ======================================================================
# Función auxiliar para el algoritmo de Dijkstra que selecciona el nodo con la distancia mínima
# @param dist: Lista de distancias.
# @param visited: Lista de nodos visitados.
# @return: El nodo con la distancia más corta de los nodos no visitados.
# ======================================================================

def min_distance_node(dist, visited):
    # Inicializa el valor mínimo y el índice del nodo mínimo.
    min_val = float("inf")
    min_index = -1

    # Itera sobre todos los nodos.
    for i in range(len(dist)):
        
        # Si el nodo no ha sido visitado y su distancia es menor que el valor mínimo actual,
        # actualiza el valor mínimo y el índice del nodo mínimo.
        if not visited[i] and dist[i] < min_val:
            min_val = dist[i]
            min_index = i

    return min_index

# ======================================================================
# Función que implementa el algoritmo de Floyd
# @param graph: Matriz de adyacencia del grafo.
# @return: Matriz de distancias más cortas entre todos los pares de nodos.
# ======================================================================

def floyd(graph):
    # Obtiene el número de nodos en el grafo.
    n = len(graph)

    # Inicializa la matriz de distancias con valores infinitos para caminos no existentes 
    # y los valores de adyacencia directa para los caminos existentes.
    dist = [[float("inf") if val == -1 else val for val in row] for row in graph]

    # La distancia de un nodo a sí mismo es siempre 0.
    for i in range(n):
        dist[i][i] = 0

    # Aplica el algoritmo de Floyd.
    # Para cada nodo intermedio 'k', actualiza las distancias más cortas entre cada par de nodos 'i' y 'j'.
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

# ========================== FUNCIÓN PRINCIPAL ==========================

def main():
    # Solicita al usuario el número total de nodos en el grafo.
    n = int(input("Ingresa el número de nodos: ").strip())

    # Solicita al usuario la matriz de adyacencia del grafo, una fila a la vez.
    print("Ingresa la matriz de adyacencia (una fila por línea):")
    graph = []  # Almacena la matriz de adyacencia.
    for _ in range(n):
        row = list(map(int, input().split()))  # Lee y convierte una fila a una lista de enteros.
        graph.append(row)  # Añade la fila a la matriz de adyacencia.

    print("\nDijkstra:")
    # Usa el algoritmo de Dijkstra para calcular y mostrar las distancias más cortas
    # desde cada nodo origen hacia todos los demás nodos.
    for i in range(n):
        distances = dijkstra(graph, i)  # Calcula las distancias desde el nodo 'i'.
        for j in range(n):
            if i != j:  # Evita mostrar la distancia de un nodo a sí mismo.
                print(f"node {i+1} to node {j+1}: ", distances[j])

    print("\nFloyd:")
    # Usa el algoritmo de Floyd-Warshall para calcular y mostrar la matriz de distancias más cortas
    # entre todos los pares de nodos.
    distances = floyd(graph)
    for i in range(n):
        print(" ".join(str(val) for val in distances[i]))  # Muestra cada fila de la matriz de distancias.

if __name__ == "__main__":
    main()