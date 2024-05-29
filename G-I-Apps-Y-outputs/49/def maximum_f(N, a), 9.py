
def maximum_f(N, a):
    max_f = 0
    for i in range(1, max(a)*2):
        f_m = sum(i % x for x in a)
        max_f = max(max_f, f_m)
    return max_f

# Read input from Standard Input
N = int(input())
a = list(map(int, input().split()))

# Calculate and print the maximum value of f
print(maximum_f(N, a))
```
