
def calculate_profit(x, p):
    expected_profit = 2 * p - (1 - p) * (1 + x/100)
    return max(0, expected_profit)

# Input
x, p = map(float, input().split())

# Calculate and output the maximum expected profit
result = calculate_profit(x, p)
print("{:.3f}".format(result))
```
