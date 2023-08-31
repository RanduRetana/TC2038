
#======================================================================
# Actividad: Actividad 1.1. Planteamiento e Implementación de algoritmos
# 
# Fecha: 16/8/2023
#
# Autores:
# Frida Bailleres González  | A01708633
# Marco Randu Retana Vargas | A01709521
# Sebastian Flores Lemus    | A01709229
#
# Descripcion: 
#En una maquila, un supervisor de producción registra la cantidad de producto
#terminado (camisas) que cada línea de producción genera durante un día
#completo de trabajo. Se tienen 2 líneas de producción que, por diversas
#razones, no necesariamente producen la misma cantidad diaria del producto.
#
#Se desea tener un programa que permita saber en cuantos días
#es posible surtir un pedido de N camisas. Con la intención de
#mejorar la planeación de los tiempos de entrega y de los insumos
#necesarios para producirlas ya que últimamente se han registrado
#retrasos en los tiempos de entrega.
# 
# ======================================================================

import math 

# ======================================================================
# Permita saber en cuantos días es posible surtir un pedido de N camisas (Python)
#
# @param lineaA, cantidad de producto terminado [camisas] de primera línea de producción.
# @param lineaB, cantidad de producto terminado [camisas] de segunda línea de producción.
# @param pedidoCantidad, cantidad de camisas del pedido.
# retorno [camisas], se regresa el número de días necesarios para surtir el pedido.
# =====================================================================


def dias_necesarios(lineaA, lineaB, pedidoCantidad):
    produccion_total = lineaA + lineaB 
    dias =  pedidoCantidad / produccion_total  
    return dias 
    
def main():
    lineaA = int(input("producción de línea A: "))  
    lineaB = int(input("producción de línea B:  "))  
    pedidoCantidad = int(input("pedido total: "))

    dias = math.ceil(dias_necesarios(lineaA, lineaB, pedidoCantidad))
    print(f"El total para surtir el pedido es de: {dias:.2f} días.")
main()