
def evaluate_expression(a, b):
    result = 0
    for i in range(1, a+1):
        result += pow(i, b, a)
    return result % a

# Read input values
a, b = map(int, input().split())

# Call the function and print the result
print(evaluate_expression(a, b))
```
