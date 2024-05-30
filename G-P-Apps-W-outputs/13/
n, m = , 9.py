
n, m = map(int, input().split())

min_cost = float('inf')
for _ in range(n):
    a, b = map(int, input().split())
    cost_per_kilo = a / b
    min_cost = min(min_cost, cost_per_kilo)

total_cost = min_cost * m
print("{:.8f}".format(total_cost))
```
