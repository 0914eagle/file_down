
def evaluate_expression(a, b):
    total = 0
    for i in range(1, a+1):
        total += pow(i, b, a)
    return total % a

# Reading input values
a, b = map(int, input().split())

# Calling the function and printing the result
print(evaluate_expression(a, b))
```
