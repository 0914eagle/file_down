
def takoyaki_health_points(N, d):
    total_health_points = 0
    for i in range(N):
        for j in range(i + 1, N):
            total_health_points += d[i] * d[j]
    return total_health_points

# Read input
N = int(input())
d = list(map(int, input().split()))

# Calculate and print the result
result = takoyaki_health_points(N, d)
print(result)
```
