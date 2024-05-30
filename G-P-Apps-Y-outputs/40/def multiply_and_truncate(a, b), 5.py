
def multiply_and_truncate(a, b):
    result = int(a * float(b))
    print(result)

if __name__ == "__main__":
    input_values = input().split()
    A = int(input_values[0])
    B = float(input_values[1])
    
    multiply_and_truncate(A, B)
```
