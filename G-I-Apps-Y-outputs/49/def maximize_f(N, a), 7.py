
def maximize_f(N, a):
    max_f = 0
    for m in range(1, max(a)*N):
        current_f = sum(m % ai for ai in a)
        max_f = max(max_f, current_f)
    return max_f

# Read input from Standard Input
N = int(input())
a = list(map(int, input().split()))

# Calculate and print the maximum value of f
print(maximize_f(N, a))
```
