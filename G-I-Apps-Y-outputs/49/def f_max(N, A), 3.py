
def f_max(N, A):
    max_val = 0

    for i in range(1, max(A)*N+1):
        current_val = sum(i % a for a in A)
        max_val = max(max_val, current_val)

    return max_val

# Sample Input
N = 3
A = [3, 4, 6]

print(f_max(N, A))
```
