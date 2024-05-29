
def max_f(N, a):
    max_val = max(a) - 1
    return sum(max_val % ai for ai in a)

# Input
N = int(input())
a = list(map(int, input().split()))

# Output
print(max_f(N, a))
```
