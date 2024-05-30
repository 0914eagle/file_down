
def calculate_profit_percentage(x, p):
    profit = (1 - p + p*x/100) / 2
    return max(0, profit) * 100

x, p = map(float, input().split())
result = calculate_profit_percentage(x, p)
print("{:.3f}".format(result))
```
