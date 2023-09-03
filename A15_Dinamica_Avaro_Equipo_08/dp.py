

#dynamic programming solution for change problem
def cambioDeMonedasDP():
    coinValues = []
    numberOfCoins = int(input("Enter the number of coins: "))
    
    for i in range(numberOfCoins):
        coin = int(input("Enter the value of the coin: "))
        coinValues.append(coin)

    price = int(input("Enter the price of the item: "))
    paid = int(input("Enter the amount paid: "))

    if paid < price:
        print("The paid amount is less than the price.")
        return

    left = paid - price
    coinValues.sort(reverse=True)
    
    dp = [float('inf')] * (left + 1)
    dp[0] = 0

    for coin in coinValues:
        for amount in range(coin, left + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

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

                    

    
            