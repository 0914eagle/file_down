
def min_bags_needed(n, k, a):
    bags = 0
    extra = 0
    
    for i in range(n):
        total = a[i] + extra
        bags += total // k
        extra = total % k
        if extra > 0:
            extra -= 1
    
    if extra > 0:
        bags += 1
    
    return bags

# Input parsing
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the output
print(min_bags_needed(n, k, a))
```
