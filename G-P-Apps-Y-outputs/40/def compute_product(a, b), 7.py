
def compute_product(a, b):
    result = int(a * b)
    print(result)

# Read input
A, B = map(float, input().split())

# Truncate B to remove decimal places
B = int(B * 100) / 100

compute_product(A, B)
```
