
def compute_truncated_product(a, b):
    result = a * float(b)
    result_int = int(result)
    print(result_int)

# Read input from Standard Input
a, b = map(str, input().split())

# Extract integer part of b
b_int = int(b.split('.')[0])

# Call the function with integer values
compute_truncated_product(int(a), b_int)
```
