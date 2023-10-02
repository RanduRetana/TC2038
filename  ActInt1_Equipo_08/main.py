# ========================== FUNCIONES AUXILIARES ==========================

# ======================================================================
# Función que construye la tabla de prefijos para KMP
#
# @param pattern: El patrón para el que se construye la tabla.
# @return: Una lista que contiene la tabla de prefijos.
# Complejidad: O(n), donde n es la longitud del patrón.
# ======================================================================

def build_kmp_table(pattern):
    table = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = table[j - 1]
        if pattern[i] == pattern[j]:
            j += 1
        table[i] = j
    return table

# ======================================================================
# Función que realiza una búsqueda de patrón utilizando KMP
#
# @param pattern: El patrón que se busca en el texto.
# @param text: El texto en el que se realiza la búsqueda.
# @return: Una lista de índices donde se encontró el patrón en el texto.
# Complejidad: O(m + n), donde m es la longitud del patrón y n es la longitud del texto.
# ======================================================================


def kmp_search(pattern, text):
    indices = []
    table = build_kmp_table(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = table[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            indices.append(i - j + 1)
            j = table[j - 1]
    return indices

# ========================== PARTE 1: Búsqueda de Códigos Maliciosos ==========================

# ======================================================================
# Función que busca códigos maliciosos en transmisiones.
#
# @return: Una lista de las transmisiones procesadas.
# Complejidad: O(n * m), donde n es la longitud total de las transmisiones y m es la longitud total de los códigos maliciosos.
# ======================================================================


def search_mcodes_in_transmissions():
    transmissions = [open(f"transmission{i}.txt", "r").read() for i in range(1, 3)]
    mcodes = [open(f"mcode{i}.txt", "r").read() for i in range(1, 4)]

    for i, mcode in enumerate(mcodes):
        for j, transmission in enumerate(transmissions):
            print(f"mcode{i+1} in transmission{j+1}")
            indices = kmp_search(mcode, transmission)
            if indices:
                for index in indices:
                    print("True", index + 1, index + len(mcode))
            else:
                print("False")
    return transmissions

# ========================== PARTE 2: Palíndromos más largos ==========================

# ======================================================================
# Función que busca el palíndromo más largo en una transmisión.
#
# @param transmission: La transmisión en la que se busca el palíndromo.
# @return: None
# Complejidad: O(n^3), donde n es la longitud de la transmisión.
# ======================================================================

def mirroredSubStringSearch(transmission):
    longestMirrored = ""
    for i in range(len(transmission)):
        for j in range(i + 1, len(transmission) + 1):
            substring = transmission[i:j]
            if substring[::-1] in transmission and len(substring) > len(longestMirrored):
                longestMirrored = substring
    print(longestMirrored, transmission.find(longestMirrored), transmission.find(longestMirrored) + len(longestMirrored) - 1)

# ========================== PARTE 3: Substring común más largo ==========================

# ======================================================================
# Función que encuentra el substring común más largo entre dos transmisiones.
#
# @param transmission1: La primera transmisión.
# @param transmission2: La segunda transmisión.
# @return: None
# Complejidad: O(m * n), donde m es la longitud de transmission1 y n es la longitud de transmission2.

def longest_common_substring(transmission1, transmission2):
   
    m, n = len(transmission1), len(transmission2)
    LCSuff = [[0 for j in range(n+1)] for i in range(m+1)]
    length = 0
    row, col = 0, 0
    
    for i in range(1, m+1):
        for j in range(1, n+1):
            if transmission1[i-1] == transmission2[j-1]:
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                if LCSuff[i][j] > length:
                    length = LCSuff[i][j]
                    row = i
                    col = j
            else:
                LCSuff[i][j] = 0
                
    if length == 0:
        print("No common substring found.")
        return

    start = row - length
    print("Longest common substring:", transmission1[start:row])
    print("Positions in transmission1:", start + 1, start + length)  

# ========================== FUNCIÓN PRINCIPAL ==========================
def _main_():

    print("\n---------------")
    print("    PARTE 1")
    print("---------------")
    transmissions = search_mcodes_in_transmissions() 

    print("\n---------------")
    print("    PARTE 2")
    print("---------------")
    print("Longest mirrored substring in transmission 1:")
    mirroredSubStringSearch(transmissions[0])
    print("\nLongest mirrored substring in transmission 2:")
    mirroredSubStringSearch(transmissions[1])

    print("\n---------------")
    print("    PARTE 3")
    print("---------------")
    longest_common_substring(transmissions[0], transmissions[1])


if __name__ == "__main__":
    _main_()