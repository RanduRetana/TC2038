#======================================================================
# Actividad: Actividad 1.5. Implementación de la técnica de programación "Programación dinámica" y "algoritmos avaros"
# 
# Fecha: 4/9/2023
#
# Autores:
# Frida Bailleres González  | A01708633
# Marco Randu Retana Vargas | A01709521
# Sebastian Flores Lemus    | A01709229
#
# Descripcion: 
#Utilizando la técnica de programación "algoritmos avaros", 
#escribe un programa que resuelva el problema del cambio de monedas.
#
#El programa recibe un numero entero N, seguido de N valores enteros (uno en cada línea,
#no necesariamente están ordenados)que representan las diferentes denominaciones disponibles
#de las monedas. Seguido de esto, el programa recibe dos números enteros: P y Q, (uno en cada línea) 
#por la entrada estándar, que representan P: el precio de un producto dado y Q: es el billete
#o moneda con el que se paga dicho producto.
#
#La salida del programa es una lista de N valores correspondientes al número de monedas de cada denominación,
#de mayor a menor, una en cada línea, que se tienen que dar para dar el cambio por el producto pagado
#utilizando un algoritmo avaro. 
# 
# ======================================================================



# ======================================================================
# Permite saber la cantidad de monedas necesarias para dar cambio
#
# @param  coinValues, lista de valores de las monedas
# @param  changePerCoin, diccionario con el número de monedas por valor
# @param numberOfCoins, número de monedas
# retorno {changePerCoin}, diccionario con el número de monedas por valor para dar el cambio necesario
#
#Complejidad: O(n), donde n es la longitud del rango.
# =====================================================================


#Función que calcula el cambio de monedas
def cambioDeMonedas():
    coinValues = []
    changePerCoin = {}

    #Se pide el número de monedas
    numberOfCoins: int = input("Enter the number of coins: ")

    #Se piden los valores de las monedas
    for i in range(int(numberOfCoins)):
        coin: int = int(input("Enter the value of the coin: "))  
        coinValues.append(coin)

    #Se ordenan los valores de las monedas de mayor a menor
    coinValues.sort(reverse=True)

    #Se piden el precio total y la cantidad que se pagó
    price: int = int(input("Enter the price of the item: "))  
    paid: int = int(input("Enter the amount paid: "))  

    #Se verifica que la cantidad pagada sea mayor o igual al precio
    if paid < price:
        print("The paid amount is less than the price.")
        return

    #Se calcula el cambio    
    left: int = paid - price

    #Se calcula el cambio por moneda
    while left != 0 and coinValues:
        if left - coinValues[0] >= 0:
            left = left - coinValues[0]
            if coinValues[0] in changePerCoin:
                changePerCoin[coinValues[0]] += 1
            else:
                changePerCoin[coinValues[0]] = 1
        else:
            coinValues.pop(0)

    #Se imprime el cambio
    if left != 0:
        print("Cannot give exact change with available coins.")
    else:
        print(changePerCoin)


cambioDeMonedas()