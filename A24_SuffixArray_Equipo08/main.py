#======================================================================
# Actividad: Actividad 2.4. Implementación de "Suffix Array"
# 
# Fecha: 24/9/2023
#
# Autores:
# Frida Bailleres González  | A01708633
# Marco Randu Retana Vargas | A01709521
# Sebastian Flores Lemus    | A01709229
#
# Descripcion: 
#Utilizando la técnica de suffix array
#Escribe un programa que dado un string, se calcule el arreglo de substrings y lo muestre ordenado alfabéticamente.
# El programa recibe un string por la entrada estándar y muestra el arreglo de substrings ordenado alfabéticamente.
#
# ======================================================================


# ======================================================================
# Permite obtener el arreglo de sufijos de un string
# @param string, string del cual se obtendrá el arreglo de sufijos
# retorno {sortedSuffixes}, arreglo de sufijos ordenado alfabéticamente
#
def suffix_array(string):
    sortedSuffixes = sorted([string[i:] for i in range(len(string))])
    return sortedSuffixes

inputString = input("Enter a string: ")
print(suffix_array(inputString))