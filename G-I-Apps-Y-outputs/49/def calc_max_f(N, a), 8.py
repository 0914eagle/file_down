
def calc_max_f(N, a):
    max_f = 0
    for i in range(1, max(a)*N+1):
        f = sum(i % x for x in a)
        max_f = max(max_f, f)
    return max_f

# Input processing
N = int(input())
a = list(map(int, input().split()))

# Calculate and print the maximum value of f
print(calc_max_f(N, a))
```
