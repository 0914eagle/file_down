
def maximum_profit(n, snacks):
    max_profit = 0
    for i in range(n):
        visited = [False] * n
        total_price = 0
        total_market_price = 0
        j = i
        while not visited[j]:
            visited[j] = True
            total_price += snacks[j][1]
            total_market_price += snacks[j][2]
            j = snacks[j][0] - 1
        profit = total_market_price - total_price
        max_profit = max(max_profit, profit)
    return max_profit

# Input parsing
n = int(input())
snacks = []
for _ in range(n):
    f, p, m, s = map(int, input().split())
    snacks.append((f, p, m, s))

# Call the function and output the result
print(maximum_profit(n, snacks))
```
