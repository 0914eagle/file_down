
def find_max_f(N, A):
    max_f = 0
    for m in range(1, max(A)*N):
        current_f = sum(m % a for a in A)
        max_f = max(max_f, current_f)
    return max_f

# Read input
N = int(input())
A = list(map(int, input().split()))

# Find and output the maximum value of f
print(find_max_f(N, A))
```
