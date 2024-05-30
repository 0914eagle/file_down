
def evaluate_expression(a, b):
    result = 0
    for i in range(1, a+1):
        result += i ** b
    return result % a

# Read input values
a, b = map(int, input().split())

# Check if b is odd
if b % 2 != 0:
    print(evaluate_expression(a, b))
else:
    print("b should be an odd number.")

```
