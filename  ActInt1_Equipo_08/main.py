# ========================== FUNCIONES AUXILIARES ==========================
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
def mirroredSubStringSearch(transmission):
    longestMirrored = ""
    for i in range(len(transmission)):
        for j in range(i + 1, len(transmission) + 1):
            substring = transmission[i:j]
            if substring[::-1] in transmission and len(substring) > len(longestMirrored):
                longestMirrored = substring
    print(longestMirrored, transmission.find(longestMirrored), transmission.find(longestMirrored) + len(longestMirrored) - 1)

# ========================== PARTE 3: Substring común más largo ==========================
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
def __main__():

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
    __main__()
