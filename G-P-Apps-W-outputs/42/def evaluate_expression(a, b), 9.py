
def evaluate_expression(a, b):
    result = 0
    for i in range(1, a+1):
        result = (result + i**b) % a
    return result

# Input
a, b = map(int, input().split())

# Output
print(evaluate_expression(a, b))
```
