
n, m = map(int, input().split())
prices = []
for _ in range(n):
    a, b = map(int, input().split())
    prices.append(a / b)

min_cost = min(prices) * m
print('{:.8f}'.format(min_cost))
```
