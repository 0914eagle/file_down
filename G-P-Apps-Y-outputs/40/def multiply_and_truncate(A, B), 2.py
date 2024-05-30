
def multiply_and_truncate(A, B):
    result = A * float(B)
    truncated_result = int(result)
    print(truncated_result)

# Read input
A, B = input().split()
A = int(A)
B = float(B)

# Call the function
multiply_and_truncate(A, B)
```
