
def min_distance_sum(n, x, v):
    total_sum = 0
    for i in range(n):
        for j in range(i + 1, n):
            min_distance = abs(x[j] - x[i]) / abs(v[i] - v[j])
            total_sum += min_distance
    return total_sum

n = int(input())
x = list(map(int, input().split()))
v = list(map(int, input().split()))

print(min_distance_sum(n, x, v))
```
