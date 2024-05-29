
def find_max_f(N, A):
    max_f = 0
    for m in range(1, 2*max(A)):
        f_val = sum(m % a for a in A)
        max_f = max(max_f, f_val)
    return max_f

# Input
N = int(input())
A = list(map(int, input().split()))

# Output
print(find_max_f(N, A))
```
