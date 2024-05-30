
def compute_product(A, B):
    product = A * float(B)
    truncated_product = int(product)
    print(truncated_product)

input_str = input()
A, B = map(str, input_str.split())
A = int(A)
B = float(B)
compute_product(A, B)
```
