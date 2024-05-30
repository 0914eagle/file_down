
def evaluate_expression(a, b):
    result = 0
    for i in range(1, a+1):
        result += i**b
    return result % a

# Input
a, b = map(int, input().split())

# Output
print(evaluate_expression(a, b))
```
