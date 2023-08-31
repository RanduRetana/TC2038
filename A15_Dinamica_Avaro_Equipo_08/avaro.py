

def cambioDeMonedas():
    coinValues = []
    changePerCoin = {}
    numberOfCoins: int = input("Enter the number of coins: ")
    for i in range(int(numberOfCoins)):
        coin: int = int(input("Enter the value of the coin: "))  
        coinValues.append(coin)

    coinValues.sort(reverse=True)
    price: int = int(input("Enter the price of the item: "))  
    paid: int = int(input("Enter the amount paid: "))  

    if paid < price:
        print("The paid amount is less than the price.")
        return
        
    left: int = paid - price
    while left != 0 and coinValues:
        if left - coinValues[0] >= 0:
            left = left - coinValues[0]
            if coinValues[0] in changePerCoin:
                changePerCoin[coinValues[0]] += 1
            else:
                changePerCoin[coinValues[0]] = 1
        else:
            coinValues.pop(0)

    if left != 0:
        print("Cannot give exact change with available coins.")
    else:
        print(changePerCoin)


cambioDeMonedas()