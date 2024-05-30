
def calculate_expression(a, b):
    result = 0
    for i in range(1, a+1):
        result += pow(i, b, a)
    return result % a

# Reading input values
a, b = map(int, input().split())

# Calling the function with input values and printing the result
print(calculate_expression(a, b))
```
