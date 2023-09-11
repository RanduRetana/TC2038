#======================================================================
# Actividad: Solución de laberinto utilizando técnicas de backtracking y ramificación y poda
# 
# Fecha: 10/9/2023
#
# Autores:
# Frida Bailleres González  | A01708633
# Marco Randu Retana Vargas | A01709521
# Sebastian Flores Lemus    | A01709229
#
# Descripción:
# El programa busca una solución para un laberinto utilizando técnicas
# de ramificación y poda. Se inicia en la casilla (0,0)
# y se busca alcanzar la casilla final (M-1, N-1). Se usa 1 para
# representar casillas transitables y 0 para las que no lo son.
#
#======================================================================


import heapq


# @param None
# @return None
#
# Descripción:
# Esta función resuelve un laberinto utilizando la técnica de ramificación
# y poda. Comienza en la casilla de inicio (0,0) y busca encontrar un
# camino hasta la casilla de salida (M-1, N-1). El laberinto se ingresa
# a través de la entrada estándar, y se muestra la solución o un mensaje
# de "No hay solución" en la salida estándar.
#
# Complejidad: O(M * N), donde M es el número de filas y N es el número de columnas del laberinto.
# ======================================================================
def resolver_laberinto():

    def es_valida(x, y):
        return 0 <= x < M and 0 <= y < N and maze[x][y] == 1

    def expandir(x, y, camino_actual):
        movimientos = [(0, 1), (1, 0)]  # Derecha y abajo

        for dx, dy in movimientos:
            nx, ny = x + dx, y + dy

            if es_valida(nx, ny) and (nx, ny) not in camino_actual:
                nuevo_camino = camino_actual + [(nx, ny)]
                nuevo_costo = len(nuevo_camino)  # Costo es la longitud del camino
                heapq.heappush(cola_prioridad, (nuevo_costo, nx, ny, nuevo_camino))

    M = int(input("Ingrese el número de filas (M): "))
    N = int(input("Ingrese el número de columnas (N): "))

    maze = []
    print("Ingrese los valores del laberinto (0 o 1) para cada celda, separados por espacio, fila por fila:")
    for _ in range(M):
        maze.append(list(map(int, input().strip().split())))

    cola_prioridad = []
    heapq.heappush(cola_prioridad, (1, 0, 0, [(0, 0)]))  # Coste, coordenadas x, coordenadas y, camino

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

resolver_laberinto()
