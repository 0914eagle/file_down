
def count_complete_figures(N, parts):
    mod = 998244353
    total = sum(parts)
    result = 1
    for i in range(1, N + 1):
        result = result * (total - i + 1) % mod
    return result

# Read input
N = int(input())
parts = list(map(int, input().split()))

# Calculate and print the result
result = count_complete_figures(N, parts)
print(result)
```
