
def solve_frane_problem(N):
    counter = 0
    for i in range(N - 1, 0, -1):
        counter += 1
        if N % i == 0:
            break
    return counter

N = int(input())
result = solve_frane_problem(N)
print(result)
```
