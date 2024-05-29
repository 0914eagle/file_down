
def min_distance_sum(n, x, v):
    total_sum = 0
    total_v = sum(v)
    
    for i in range(n):
        total_sum += x[i] * total_v
        total_v -= v[i]
    
    return total_sum

# Input parsing
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

# Call the function and print the output
print(min_distance_sum(n, x, v))
```
