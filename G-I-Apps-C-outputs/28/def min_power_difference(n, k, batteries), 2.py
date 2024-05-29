
def min_power_difference(n, k, batteries):
    batteries.sort()
    min_diff = float('inf')
    
    for i in range(n):
        chip1_powers = batteries[i*k: (i+1)*k]
        chip2_powers = batteries[(n+i)*k: (n+i+1)*k]
        
        diff = max(abs(a - b) for a in chip1_powers for b in chip2_powers)
        min_diff = min(min_diff, diff)
    
    return min_diff

# Read input
n, k = map(int, input().split())
batteries = list(map(int, input().split()))

# Output the result
print(min_power_difference(n, k, batteries))
```
