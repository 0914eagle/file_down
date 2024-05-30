
def evaluate_expression(a, b):
    total = 0
    for i in range(1, a+1):
        total += i**b
    return total % a

# Read input values
a, b = map(int, input().split())

# Evaluate the expression and print the result
result = evaluate_expression(a, b)
print(result)
```
