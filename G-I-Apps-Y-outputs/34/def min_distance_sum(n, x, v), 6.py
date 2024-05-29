
def min_distance_sum(n, x, v):
    total_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = abs(x[i] - x[j]) / abs(v[i] - v[j])
            total_sum += min((dist * v[i] + x[i]) - x[i], (dist * v[j] + x[j]) - x[j])
    return total_sum

# Input
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

# Output
print(min_distance_sum(n, x, v))
```
