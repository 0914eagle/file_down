
def minimum_distance_sum(n, x, v):
    def min_distance(xi, vi, xj, vj):
        if vi == vj:
            return abs(xi - xj)
        return abs((xi - xj) / (vj - vi))
    
    total_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            total_sum += min_distance(x[i], v[i], x[j], v[j])
    
    return int(total_sum)

# Read input
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

# Calculate and print the minimum distance sum
print(minimum_distance_sum(n, x, v))
```
