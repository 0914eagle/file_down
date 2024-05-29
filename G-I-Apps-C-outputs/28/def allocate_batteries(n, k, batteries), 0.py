
def allocate_batteries(n, k, batteries):
    batteries.sort()
    diffs = [(batteries[i+k-1] - batteries[i]) for i in range(k)]
    return max(diffs) // 2

# Input parsing
n, k = map(int, input().split())
batteries = list(map(int, input().split()))

# Output
print(allocate_batteries(n, k, batteries))
```
