
def franes_program(N):
    counter = 0
    for i in range(N - 1, 0, -1):
        counter += 1
        if N % i == 0:
            break
    return counter

N = int(input())
output = franes_program(N)
print(output)
```
