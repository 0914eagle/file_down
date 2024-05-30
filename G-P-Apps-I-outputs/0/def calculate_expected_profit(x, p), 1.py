
def calculate_expected_profit(x, p):
    expected_profit = 0.0
    for i in range(1, 1001):
        expected_profit += max(2*(p/100) - 1 - x/100, 0)
    return round(expected_profit, 3)

# Reading input
x, p = map(float, input().split())

# Calculating and printing the maximum expected profit
print(calculate_expected_profit(x, p))
```
