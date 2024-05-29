
def calculate_f(N, a):
    max_f = 0
    for m in range(max(a), sum(a)):
        current_f = sum(m % ai for ai in a)
        max_f = max(max_f, current_f)
    return max_f

# Read input values
N = int(input())
a = list(map(int, input().split()))

# Calculate and print the maximum value of f
print(calculate_f(N, a))
```
