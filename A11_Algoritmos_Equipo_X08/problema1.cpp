// ======================================================================
// Actividad: Actividad 1.1. Planteamiento e Implementación de algoritmos
// 
// Fecha: 16/8/2023
//
// Autores:
// Frida Bailleres González  | A01708633
// Marco Randu Retana Vargas | A01709521
// Sebastian Flores Lemus    | A01709229
//
// Descripcion: 
//En una maquila, un supervisor de producción registra la cantidad de producto
//terminado (camisas) que cada línea de producción genera durante un día
//completo de trabajo. Se tienen 2 líneas de producción que, por diversas
//razones, no necesariamente producen la misma cantidad diaria del producto.
//
//Se desea tener un programa que permita saber en cuantos días
//es posible surtir un pedido de N camisas. Con la intención de
//mejorar la planeación de los tiempos de entrega y de los insumos
//necesarios para producirlas ya que últimamente se han registrado
//retrasos en los tiempos de entrega.
//
// ======================================================================

#include <iostream>

using namespace std;

// ======================================================================
// Permita saber en cuantos días es posible surtir un pedido de N camisas (C++)
//
// @param lineaA, cantidad de producto terminado (camisas) de primera línea de producción.
// @param lineaB, cantidad de producto terminado (camisas) de segunda línea de producción.
// @param pedidoCantidad, cantidad de camisas del pedido.
// retorno (int), se regresa el número de días necesarios para surtir el pedido.
// complejidad: O(n) donde "n" representa la cantidad total de unidades en el pedido.
// =====================================================================

int maquila(int lineaA, int lineaB, int pedidoCantidad) {
    int dias = 0;
    
    while (pedidoCantidad > 0) {
        int produccionDiaA = (pedidoCantidad >= lineaA) ? lineaA : pedidoCantidad;
        int produccionDiaB = (pedidoCantidad - produccionDiaA >= lineaB) ? lineaB : pedidoCantidad - produccionDiaA;
        
        pedidoCantidad -= (produccionDiaA + produccionDiaB);
        dias++;
    }
    
    return dias;
}

int main() {
    int cantidadLineaA = 100;
    int cantidadLineaB = 214;
    int totalPedido = 2000;
    
    int res = maquila(cantidadLineaA, cantidadLineaB, totalPedido);
    
    cout << "El total para surtir el pedido es de: " << res << " días." << endl;

    return 0;
}