
def max_profit(n, snacks):
    max_profit = 0
    for i in range(n):
        visited = [False] * n
        j = i
        total_cost = 0
        total_profit = 0
        while not visited[j]:
            visited[j] = True
            total_cost += snacks[j][1]
            total_profit += snacks[j][2] - snacks[j][1]
            j = snacks[j][0] - 1
        if total_profit > 0:
            cycles = total_cost // total_profit
            remaining_cost = total_cost % total_profit
            max_profit = max(max_profit, (cycles * total_profit) + (cycles * remaining_cost))
    return max_profit

# Read input
n = int(input())
snacks = []
for _ in range(n):
    f, p, m, s = map(int, input().split())
    snacks.append((f, p, m, s))

# Calculate and output the result
result = max_profit(n, snacks)
print(result)
```
