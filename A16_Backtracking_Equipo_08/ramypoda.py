# ======================================================================
# Actividad:  Actividad 1.6 Implementación de la técnica de programación "backtracking" y "ramificación y poda"
# 
# Fecha: 10/9/2023
# 
# Autores:
# Frida Bailleres González  | A01708633
# Marco Randu Retana Vargas | A01709521
# Sebastian Flores Lemus    | A01709229
#
# Descripción: Este programa busca resolver un laberinto representado por una 
# matriz de MxN utilizando el método de Ramificación y Poda. El laberinto es 
# ingresado por el usuario fila por fila, donde 1 representa un camino transitable 
# y 0 un obstáculo. El programa busca el camino más corto desde el inicio (0,0) 
# hasta el final (M-1, N-1), moviéndose solo hacia la derecha o hacia abajo. 
# Utiliza una cola de prioridad para determinar el siguiente nodo a expandir 
# basándose en el costo del camino actual.
# Complejidad: O(MN log(MN)), siendo MN el número total de nodos posibles
# en el laberinto.
# ======================================================================

import heapq

def resolver_laberinto():
    # ======================================================================
    # Función auxiliar para verificar si una celda es válida.
    #
    # @param x: La coordenada x de la celda.
    # @param y: La coordenada y de la celda.
    # @return: Verdadero si la celda es válida, falso de lo contrario.
    # Complejidad: O(1), verificación constante de las condiciones.
    # ======================================================================
    def es_valida(x, y):
        return 0 <= x < M and 0 <= y < N and maze[x][y] == 1

    # ======================================================================
    # Función auxiliar para expandir un nodo y añadir los nodos resultantes
    # a la cola de prioridad.
    #
    # @param x: La coordenada x del nodo actual.
    # @param y: La coordenada y del nodo actual.
    # @param camino_actual: Lista de tuplas que representa el camino actual.
    # Complejidad: O(1), ya que solo considera dos movimientos posibles.
    # ======================================================================
    def expandir(x, y, camino_actual):
        movimientos = [(0, 1), (1, 0)]  # Derecha y abajo

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy

            if es_valida(nx, ny) and (nx, ny) not in camino_actual:
                nuevo_camino = camino_actual + [(nx, ny)]
                nuevo_costo = len(nuevo_camino)  # Costo es la longitud del camino
                heapq.heappush(cola_prioridad, (nuevo_costo, nx, ny, nuevo_camino))

    # ======================================================================
    # Principal cuerpo de la función resolver_laberinto.
    # El usuario ingresa el tamaño y los detalles del laberinto.
    # ======================================================================

    M = int(input("Ingrese el número de filas (M): "))
    N = int(input("Ingrese el número de columnas (N): "))

    maze = []
    print("Ingrese los valores del laberinto (0 o 1) para cada celda, separados por espacio, fila por fila:")
    for _ in range(M):
        maze.append(list(map(int, input().strip().split())))

    # Inicialización de la cola de prioridad y el primer nodo
    cola_prioridad = []
    heapq.heappush(cola_prioridad, (1, 0, 0, [(0, 0)]))  # Coste, coordenadas x, coordenadas y, camino

    # ======================================================================
    # Loop principal que explora los caminos en el laberinto utilizando
    # Ramificación y Poda hasta encontrar la solución o determinar que
    # no hay solución.
    # Complejidad: O(MN log(MN)), siendo MN el número total de nodos posibles
    # en el laberinto.
    # ======================================================================
    while cola_prioridad:
        _, x, y, camino_actual = heapq.heappop(cola_prioridad)

        if (x, y) == (M - 1, N - 1):
            print("Ramificación y Poda:")
            for i in range(M):
                for j in range(N):
                    if (i, j) in camino_actual:
                        print('1', end=' ')
                    else:
                        print('0', end=' ')
                print()
            return

        expandir(x, y, camino_actual)

    print("No hay solución")

# Llamada a la función principal para iniciar el programa
resolver_laberinto()
