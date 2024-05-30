
MOD = 998244353

def count_monotonic_renumerations(n, a):
    if n == 2:
        return 2

    counts = {}
    for num in a:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    unique_counts = set(counts.values())
    result = 1
    for count in unique_counts:
        result = (result * count) % MOD

    return result

# Reading input
n = int(input())
a = list(map(int, input().split()))

# Calculating and printing the result
print(count_monotonic_renumerations(n, a))
```
