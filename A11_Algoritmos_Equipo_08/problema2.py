
#======================================================================
# Actividad: Actividad 1.1. Planteamiento e Implementación de algoritmos
# 
# Fecha: 16/8/2023
#
# Autores:
#F rida Bailleres González  | A01708633
# Marco Randu Retana Vargas | A01709521
# Sebastian Flores Lemus    | A01709229
#
# Descripcion: 
#Resulta que ha llegado una nueva máquina embotelladora de refrescos, el contenedor
#principal de la máquina tiene forma cilíndrica. Se sabe que cada envase de refresco debe
#contener M mililitros. Se desea saber cuántos refrescos puede llenar la máquina de una
#sola vez, sin recargar el contenedor. Solo se tienen los datos del radio de la base y la
#altura medidos en metros.
# ======================================================================

import math

# ======================================================================
# Permita saber cuantas botellas de N capacidad se pueden servir de una máquina embotelladora cilíndrica de N capacidad
# @param soda_capacity , capacidad de las botellas a llenar.
# @param cylinder_volume,volumen total de la máquina embotelladora.
# @param num_sodas, cantidad de sodas que se pueden llenar.
# etorno (int), se regresa el número de sodas totales que se pueden llenar con la capacidad de la máquina.
# =====================================================================


# Function to calculate the number of sodas that can fit in a container
def calculateSodas(radius, height):
    print("The soda can has a volume of 355 milliliters")
    soda_capacity = 0.355
    # Calculate the volume of the cylindrical container using the given radius and height
    cylinder_volume = (math.pi * (radius * radius) * height)* 1000
    # Calculate the number of sodas that can fit in the container by dividing container volume by soda volume
    num_sodas = math.floor(cylinder_volume/ soda_capacity )
    # Print the container's volume and the number of sodas that can fit
    print("The volume of the container is", cylinder_volume)
    print("The number of sodas that can fit in the container is", num_sodas)

# Main function to get input and call the soda calculation function
def main():
    radius = float(input("Enter the radius of the container (meters): "))
    height = float(input("Enter the height of the container (meters): "))
    calculateSodas(radius, height)

# Call the main function to start the program
main()