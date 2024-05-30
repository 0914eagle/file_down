
def min_bags_to_dispose_garbage(n, k, a):
    bags = 0
    remaining_units = 0
    
    for i in range(n):
        total_units = a[i] + remaining_units
        bags += total_units // k
        remaining_units = total_units % k
    
    if remaining_units > 0:
        bags += 1
    
    return bags

# Input parsing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(min_bags_to_dispose_garbage(n, k, a))
```
