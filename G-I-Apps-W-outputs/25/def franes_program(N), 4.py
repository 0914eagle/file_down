
def franes_program(N):
    counter = 0
    for i in range(N - 1, 0, -1):
        counter += 1
        if N % i == 0:
            break
    return counter

# Read input
N = int(input())

# Call the function and output the result
print(franes_program(N))
```
