
def max_profit(n, snacks):
    total_profit = 0
    for i in range(n):
        visited = [False] * n
        j = i
        cycle_profit = 0
        cycle_size = 0
        min_cost = float('inf')
        while not visited[j]:
            visited[j] = True
            cycle_size += 1
            cycle_profit += snacks[j][2] - snacks[j][1]
            min_cost = min(min_cost, snacks[j][1])
            j = snacks[j][0] - 1

        if cycle_profit > 0:
            total_profit += (cycle_size - 2) * min_cost + cycle_profit

    return total_profit

# Read input
n = int(input())
snacks = []
for _ in range(n):
    f, p, m, s = map(int, input().split())
    snacks.append((f, p, m, s))

# Calculate and output the maximum profit
print(max_profit(n, snacks))
```
