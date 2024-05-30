
def max_profit(n, snacks):
    profits = [0] * n
    
    for i in range(n-1, -1, -1):
        f, p, m, s = snacks[i]
        if f < n:  # Check if the vending position is within the range
            profit = m - p
            if f < n - 1:
                profit += profits[f]
            profits[i] = max(profit, profits[i+1])
    
    return profits[0]

# Read input
n = int(input())
snacks = []
for _ in range(n):
    f, p, m, s = map(int, input().split())
    snacks.append((f, p, m, s))

# Calculate and output the maximum profit
print(max_profit(n, snacks))
```
