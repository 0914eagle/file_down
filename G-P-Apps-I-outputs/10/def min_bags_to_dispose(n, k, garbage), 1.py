
def min_bags_to_dispose(n, k, garbage):
    bags = 0
    remaining_units = 0
    
    for day in range(n):
        total_units = garbage[day] + remaining_units
        bags += total_units // k
        remaining_units = total_units % k
        
        if day == n - 1 and remaining_units > 0:
            bags += 1
    
    return bags

# Input parsing
n, k = map(int, input().split())
garbage = list(map(int, input().split()))

# Call the function and print the result
print(min_bags_to_dispose(n, k, garbage))
```
