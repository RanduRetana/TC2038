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
#Utilizando la técnica de programación "programación dinámica", 
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
#utilizando programación dinámica. 
# 
# ======================================================================


# ======================================================================
# Permite saber la cantidad de monedas necesarias para dar cambio
#
# @param  coinValues, lista de valores de las monedas
# @param numberOfCoins, número de monedas
# @param price, precio del producto
# @param paid, cantidad pagada
# @param coin, valor de la moneda
# @param change, diccionario con el número de monedas por valor
# @param left, cambio que falta por dar
# retorno {change}, diccionario con el número de monedas por valor para dar el cambio necesario
#
#Complejidad: O(n), donde n es la longitud del rango.
# =====================================================================



#dynamic programming solution for change problem
def cambioDeMonedasDP():
    coinValues = []
    numberOfCoins = int(input("Enter the number of coins: "))
    
    #Se piden los valores de las monedas
    for i in range(numberOfCoins):
        coin = int(input("Enter the value of the coin: "))
        coinValues.append(coin)

    #Se piden el precio total y la cantidad que se pagó
    price = int(input("Enter the price of the item: "))
    paid = int(input("Enter the amount paid: "))

    #Se verifica que la cantidad pagada sea mayor o igual al precio
    if paid < price:
        print("The paid amount is less than the price.")
        return
    
    #Se calcula el cambio que falta por dar
    left = paid - price
    coinValues.sort(reverse=True)#Se ordenan los valores de las monedas de mayor a menor
    
    #Se crea un arreglo de tamaño left + 1
    dp = [float('inf')] * (left + 1)
    dp[0] = 0

    #Se calcula el cambio por moneda
    for coin in coinValues:
        for amount in range(coin, left + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    #Se verifica que se pueda dar el cambio exacto
    if dp[left] == float('inf'):
        print("Cannot give exact change with available coins.")
    else:
        change = {}
        amount = left
        for coin in coinValues:
            while amount >= coin and dp[amount] == dp[amount - coin] + 1:
                if coin in change:
                    change[coin] += 1
                else:
                    change[coin] = 1
                amount -= coin
        print(change)

cambioDeMonedasDP()

                    

    
            