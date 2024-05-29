
def min_distance_sum(n, x, v):
    total_sum = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = abs(x[j] - x[i]) / (abs(v[i] - v[j]))
            total_sum += min(dist, abs(x[i] - x[j]) / abs(v[i] + v[j]))
    return int(total_sum)

# Input processing
n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

# Calculate and print the output
print(min_distance_sum(n, x, v))
```
