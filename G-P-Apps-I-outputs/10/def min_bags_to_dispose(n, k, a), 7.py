
def min_bags_to_dispose(n, k, a):
    bags_needed = 0
    remaining_garbage = 0
    
    for i in range(n):
        total_garbage = a[i] + remaining_garbage
        bags_needed += total_garbage // k
        remaining_garbage = total_garbage % k
    
    if remaining_garbage > 0:
        bags_needed += 1
    
    return bags_needed

# Input parsing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(min_bags_to_dispose(n, k, a))
```
