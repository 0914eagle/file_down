
def solve_frane_problem(N):
    counter = 0
    for i in range(N - 1, 0, -1):
        counter += 1
        if N % i == 0:
            break
    return counter

# Read input
N = int(input())
# Solve the problem
result = solve_frane_problem(N)
# Output the result
print(result)
```
