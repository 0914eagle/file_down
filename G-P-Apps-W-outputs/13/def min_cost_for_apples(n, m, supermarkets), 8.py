
def min_cost_for_apples(n, m, supermarkets):
    min_cost = float('inf')
    for a, b in supermarkets:
        cost_per_kilo = a / b
        total_cost = cost_per_kilo * m
        min_cost = min(min_cost, total_cost)
    return min_cost

# Input processing
n, m = map(int, input().split())
supermarkets = [tuple(map(int, input().split())) for _ in range(n)]

# Calculate and print the minimum cost
result = min_cost_for_apples(n, m, supermarkets)
print("{:.8f}".format(result))
```
