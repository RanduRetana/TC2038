// ======================================================================
// Actividad 1.6 Implementación de la técnica de programación "backtracking" y "ramificación y poda"
//
// Fecha: 10/09/2023
//
// Autores:
// Frida Bailleres González  | A01708633
// Marco Randu Retana Vargas | A01709521
// Sebastian Flores Lemus    | A01709229
//
// El programa busca una solución para un laberinto utilizando técnicas
// de backtracking. Se inicia en la casilla (0,0)
// y se busca alcanzar la casilla final (M-1, N-1). Se usa 1 para
// representar casillas transitables y 0 para las que no lo son.
// Complejidad: O(2^(M*N))
// ======================================================================

#include <iostream>
#include <vector>

using namespace std;

int M, N;
vector<vector<int> > maze;
vector<vector<bool> > solution;

// ======================================================================
// Función que verifica si es seguro moverse a una casilla
//
// @param x: La coordenada x de la casilla.
// @param y: La coordenada y de la casilla.
// @return True si es seguro moverse a la casilla, False en caso contrario.
// Complejidad: O(1)  ya que solo realiza operaciones básicas que toman un tiempo constante.
// =====================================================================
 
bool isSafe(int x, int y) {
    return (x >= 0 && x < M && y >= 0 && y < N && maze[x][y] == 1);
}

// ======================================================================
// Función que resuelve el laberinto utilizando la técnica de backtracking
//
// @param x: La coordenada x actual.
// @param y: La coordenada y actual.
// @return True si se encontró una solución, False en caso contrario.
// Complejidad: O(2^(M*N)), en el peor de los casos, ya que en el peor escenario exploraría todas las posibles rutas en el laberinto.
// =====================================================================

bool Backtracking(int x, int y) {
    if (x == M - 1 && y == N - 1) {
        solution[x][y] = true;
        return true;
    }

    if (isSafe(x + 1, y)) {
        solution[x][y] = true;
        if (Backtracking(x + 1, y))
            return true;
        solution[x][y] = false; 
    }

    if (isSafe(x, y + 1)) {
        solution[x][y] = true;
        if (Backtracking(x, y + 1))
            return true;
        solution[x][y] = false; 
    }

    return false; 
}

int main() {
    cout << "Ingrese el valor de M: ";
    cin >> M;
   
    while (M <= 0){
        cout << "Tiene que ser un valor mayor a 0" << endl;
        cout << "Ingrese el valor de M: ";
        cin >> M;
    }
    cout << "Ingrese el valor de N: ";
    cin >> N;
    while (N <= 0){
        cout << "Tiene que ser un valor mayor a 0" << endl;
        cout << "Ingrese el valor de N: ";
        cin >> N;
    }

    cout << "Ingrese el laberinto:" << endl;

    maze.resize(M, vector<int>(N));
    solution.resize(M, vector<bool>(N, false));

    for (int i = 0; i < M; ++i) {
        for (int j = 0; j < N; ++j) {
            while (true) {
                int value;
                cin >> value;
                if (value == 0 || value == 1) {
                    maze[i][j] = value;
                    break;
                } else {
                    cout << "Solo puedes ingresar 1 o 0" << endl;
                }
            }
        }
    }

    cout << "Backtracking:" << endl;
    if (Backtracking(0, 0)) {
        for (int i = 0; i < M; ++i) {
            for (int j = 0; j < N; ++j) {
                cout << solution[i][j] << " ";
            }
            cout << endl;
        }
    } else {
        cout << "No se encontró una solución" << endl;
    }

    return 0;
}

