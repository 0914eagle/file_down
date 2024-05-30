
def compute_truncated_product(A, B):
    product = A * float(B)
    result = int(product)
    print(result)

# Read input from Standard Input
A, B = input().split()
A = int(A)
B = float(B)

compute_truncated_product(A, B)
```
