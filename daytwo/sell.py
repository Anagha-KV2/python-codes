def maxProfit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price

        profit = price - min_price

        if profit > max_profit:
            max_profit = profit

    return max_profit

# User input
prices = list(map(int, input("Enter stock prices separated by spaces: ").split()))

print("Maximum Profit:", maxProfit(prices))