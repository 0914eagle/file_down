
def calculate_expression(a, b):
    result = 0
    for i in range(1, a+1):
        result += i ** b
    return result % a

# Read input values
a, b = map(int, input().split())

# Call the function and print the result
print(calculate_expression(a, b))
```
