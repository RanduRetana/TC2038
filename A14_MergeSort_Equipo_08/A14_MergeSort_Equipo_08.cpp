// ======================================================================
// Actividad 1.4. Implementación de la técnica de programación "divide y vencerás"
//
// Fecha: 27/8/2023
//
// Autores:
// Frida Bailleres González  | A01708633
// Marco Randu Retana Vargas | A01709521
// Sebastian Flores Lemus    | A01709229
//
// Descripcion: Este programa implementa el algoritmo de ordenaciC3n "Merge Sort"
// utilizando la técnica de programaciC3n "divide y vencerC!s". El algoritmo divide
// recursivamente el arreglo en dos mitades hasta que cada sub-arreglo contiene un C:nico elemento.
// A continuación, combina (merge) estos sub-arreglos para producir nuevos sub-arreglos ordenados.
// Estos son combinados continuamente hasta obtener un C:nico arreglo ordenado.
// ======================================================================

#include <iostream>

// ======================================================================
// Función para combinar dos sub-arrays en uno solo ordenado.
//
// @param array[]: El arreglo que contiene los sub-arrays a combinar.
// @param low: Índice del primer elemento en el rango.
// @param middle: Índice del último elemento de la primera mitad.
// @param high: Índice del último elemento en el rango.
// Complejidad: O(n), donde n es la longitud del rango.
// =====================================================================

template<class T>
void Merge(T array[], int low, int middle, int high){

    // Longitud de los dos sub-arrays.
    int length_array_left = middle - low + 1;
    int length_array_right = high - middle;

    // Crear sub-array temporales.
    T arr_left[length_array_left];
    T arr_right[length_array_right];

    // Copiar datos a los sub-arrays temporales.
    for(int i = 0; i < length_array_left; i++){
        arr_left[i] = array[low + i];
    }
    for(int j = 0; j < length_array_right; j++){
        arr_right[j] = array[middle + 1 + j];
    }

    // variables de los sub-arrays y del array combinado.
    int i, j, k;
    i = j = 0;
    k = low;

    // Combinar los sub-array.
    while(i < length_array_left && j < length_array_right){
        if(arr_left[i] <= arr_right[j]){
            array[k] = arr_left[i];
            i++;
        } else {
            array[k] = arr_right[j];
            j++;
        }
        k++;
    }
    // Copiar elementos restantes de arr_left si es que hay.
    while(i < length_array_left){
        array[k] = arr_left[i];
        i++;
        k++;
    }

    // Copiar los elementos restantes de arr_right si es que hay.
    while(j < length_array_right){
        array[k] = arr_right[j];
        j++;
        k++;
    }
}

// ======================================================================
// Función recursiva para dividir el array en dos mitades y ordenarlas.
//
// @param A[]: El arreglo que se desea ordenar.
// @param low: Índice del primer elemento en el rango.
// @param high: Índice del último elemento en el rango.
// Complejidad: O(n log n), donde n es la longitud del rango.
// =====================================================================

template<class T>
void MergeSort(T A[], int low, int high){
  if(low >= high){
      return; // Si el array tiene un solo elemento lo retorna.
  }
  int middle = low + (high - low)/2; // Encuentra el punto medio del array.
  MergeSort(A, low,middle); // Ordena la primera mitad.
  MergeSort(A, middle + 1, high); // Ordena la segunda mitad.
  Merge(A, low, middle, high); // Combina las dos mitades ya ordenadas.
}

// ======================================================================
// Función para imprimir el arreglo de Mayor a menor.
//
// @param A[]: El arreglo que se desea imprimir.
// @param n: La longitud del arreglo.
// Complejidad: O(n), donde n es la longitud del arreglo.
// =====================================================================

template<class T>

void printReverse(T A[], int n){
    for(int i = n-1; i >= 0; i--){
        std::cout << A[i] << " ";
    }
    std::cout << '\n';
}

// ======================================================================
// Función para imprimir el arreglo no ordenado.
//
// @param A[]: El arreglo que se desea imprimir.
// @param n: La longitud del arreglo.
// Complejidad: O(n), donde n es la longitud del arreglo.
// =====================================================================

template<class T>

void print(T A[], int n){
    for(int i = 0; i < n; i++){
        std::cout << A[i] << " ";
    }
    std::cout << '\n';
}

int main() {

    int array[] = {38, 27, 43, 3, 9, 82, 10};
    int n = sizeof(array)/sizeof(array[0]);
    
    std::cout << "El arreglo antes del sort es:" << std::endl;
    print(array, n);
    
    MergeSort(array, 0, n - 1);
    
    std::cout << "El arreglo ordenado es:" << std::endl;
    printReverse(array, n);
    
    int array2[] = {5, 2, 7, 6, 2, 1, 0, 3, 9, 4};
    int n2 = sizeof(array2)/sizeof(array2[0]);
    
    std::cout << "\nEl arreglo antes del sort es: " << std::endl;
    print(array2, n2);
    
    MergeSort(array2, 0, n2 - 1);
    
    std::cout << "El arreglo ordenado es:" << std::endl;
    printReverse(array2, n2);
    

    return 0;
}