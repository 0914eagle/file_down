
def min_bags(n, k, a):
    bags = 0
    remaining = 0
    
    for i in range(n):
        total_garbage = remaining + a[i]
        bags += total_garbage // k
        remaining = total_garbage % k
    
    if remaining > 0:
        bags += 1
    
    return bags

# Input processing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function
result = min_bags(n, k, a)
print(result)
```
