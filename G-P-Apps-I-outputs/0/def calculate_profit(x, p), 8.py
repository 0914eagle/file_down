
def calculate_profit(x, p):
    expected_profit = 2 * p - (1-p) * (1 + x/100)
    return max(0, expected_profit)

# Input processing
x, p = map(float, input().split())

# Call the function and display the result with precision
result = calculate_profit(x, p)
print("{:.3f}".format(result))
```
