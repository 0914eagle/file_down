
def calculate_restored_health(N, deliciousness):
    total_health_points = 0
    for i in range(N):
        for j in range(i+1, N):
            total_health_points += deliciousness[i] * deliciousness[j]
    return total_health_points

# Read input
N = int(input())
deliciousness = list(map(int, input().split()))

# Calculate and print the result
print(calculate_restored_health(N, deliciousness))
```
