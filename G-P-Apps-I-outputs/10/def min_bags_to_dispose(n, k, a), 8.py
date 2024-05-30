
def min_bags_to_dispose(n, k, a):
    bags = 0
    remaining = 0
    
    for i in range(n):
        total_garbage = a[i] + remaining
        
        bags_needed = total_garbage // k
        remaining = total_garbage % k
        
        if remaining > 0:
            bags_needed += 1
        
        bags += bags_needed
    
    if remaining > 0:
        bags += 1
    
    return bags

# Input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(min_bags_to_dispose(n, k, a))
```
