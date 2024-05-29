
def solve_problem(A, B, N):
    result = 0
    for x in range(N+1):
        value = (A*x)//B - A*(x//B)
        result = max(result, value)
    return result

# Taking input from Standard Input
A, B, N = map(int, input().strip().split())

# Calling the function and printing the result
print(solve_problem(A, B, N))
```
