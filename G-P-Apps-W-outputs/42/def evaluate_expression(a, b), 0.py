
def evaluate_expression(a, b):
    result = 0
    for i in range(1, a+1):
        result += pow(i, b, a)
    return result % a

# Input values
a, b = map(int, input().split())

# Output the result
print(evaluate_expression(a, b))
```
