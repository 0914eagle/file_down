
def calculate_profit(n, d, prices, m):
    prices.sort()
    profit = 0
    for i in range(m):
        if i < n:
            profit += prices[i]
        else:
            profit -= d
    return profit

# Input parsing
n, d = map(int, input().split())
prices = list(map(int, input().split()))
m = int(input())

# Calculate and print the profit
print(calculate_profit(n, d, prices, m))
```
