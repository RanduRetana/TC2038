# ======================================================================
# Actividad: Actividad 2.3. Implementación de "Hash String"
# 
# Fecha: 21/9/2023
# 
# Autores:
# Frida Bailleres González  | A01708633
# Marco Randu Retana Vargas | A01709521
# Sebastian Flores Lemus    | A01709229
#
# Descripción: Este programa toma un archivo de texto y un número entero
# múltiplo de 4 (entre 16 y 64) para generar un hash de longitud n/4.
# Se muestra la tabla generada, el arreglo de sumas y el hash resultante.
#
# Complejidad:La complejidad del programa es  O(m), determinada principalmente por las
# operaciones sobre la longitud del archivo "m", considerando que "n"
# (que está entre el 16 y 64) es un valor constante.
# ======================================================================

def generar_hash():
    # Solicitar datos de entrada
    nombre_archivo_sin_extension = input("Ingrese el nombre del archivo de texto (sin el .txt): ")
    nombre_archivo = nombre_archivo_sin_extension + ".txt"

    n = int(input("Ingrese un entero múltiplo de 4 (entre 16 y 64): "))
    
    # Leer archivo y guardar contenido
    with open(nombre_archivo, 'r') as archivo:
        contenido = archivo.read().replace('\n', '-')
    
    # Completar contenido con el carácter '[' si no es múltiplo de n
    while len(contenido) % n != 0:
        contenido += '['
    
    # Crear la tabla con el contenido
    tabla = [contenido[i:i+n] for i in range(0, len(contenido), n)]
    
    # Imprimir la tabla
    print("\nMatriz generada. (Saltos = '-' y espacios = '[' ): ")
    for fila in tabla:
        print(fila)
    
    # Calcular el arreglo a
    a = []
    for j in range(n):
        suma_columna = sum([ord(fila[j]) for fila in tabla]) % 256
        a.append(suma_columna)
        # La función ord() es una función que devuelve un entero 
        # representando el código Unicode del caracter proporcionado.
    
    # Imprimir el arreglo a
    print("\nArreglo a:")
    print(a)
    
    # Generar el hash
    hash_resultante = ''.join([format(valor, '02X') for valor in a])
        #   La cadena de formato '02X' es una especificación de formato utilizada
        #  con la función format() para representar un número en notación hexadecimal con letras mayúsculas. 
   
    
    # Imprimir el hash
    print("\nCadena de salid:")
    print(' '.join([hash_resultante[i:i+4] for i in range(0, len(hash_resultante), 4)]))

# Llamada a la función principal para iniciar el programa
generar_hash()
