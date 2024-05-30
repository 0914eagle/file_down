
def min_bags_to_dispose_of_garbage(n, k, a):
    bags = 0
    remaining_garbage = 0
    
    for i in range(n):
        total_garbage = a[i] + remaining_garbage
        bags += total_garbage // k
        remaining_garbage = total_garbage % k
        
        if i == n - 1:
            bags += (remaining_garbage + k - 1) // k
    
    return bags

# Reading input
n, k = map(int, input().split())
a = list(map(int, input().split()))

# Call the function and print the output
print(min_bags_to_dispose_of_garbage(n, k, a))
```
