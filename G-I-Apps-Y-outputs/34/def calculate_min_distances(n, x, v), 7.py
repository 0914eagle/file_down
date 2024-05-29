
def calculate_min_distances(n, x, v):
    total_dist = 0
    for i in range(n):
        for j in range(i+1, n):
            min_dist = abs(x[i]-x[j]) / abs(v[i]-v[j])
            total_dist += min_dist
    return int(total_dist)

# Read input
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

# Calculate and print the result
print(calculate_min_distances(n, x, v))
```
