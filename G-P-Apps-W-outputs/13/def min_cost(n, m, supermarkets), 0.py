
def min_cost(n, m, supermarkets):
    min_price = float('inf')
    for a, b in supermarkets:
        price_per_kilo = a / b
        total_price = price_per_kilo * m
        min_price = min(min_price, total_price)
    return min_price

n, m = map(int, input().split())
supermarkets = [list(map(int, input().split())) for _ in range(n)]

result = min_cost(n, m, supermarkets)
print('%.8f' % result)
```
