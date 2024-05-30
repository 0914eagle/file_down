
def min_bags_to_dispose_garbage(n, k, garbage):
    bags = 0
    remaining_garbage = 0
    for i in range(n):
        total_garbage = garbage[i] + remaining_garbage
        bags += total_garbage // k
        remaining_garbage = total_garbage % k
        if i == n - 1:
            bags += 1 if remaining_garbage > 0 else 0
    return bags

# Input parsing
n, k = map(int, input().split())
garbage = list(map(int, input().split()))

# Output
print(min_bags_to_dispose_garbage(n, k, garbage))
```
