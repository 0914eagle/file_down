
def takoyaki_festival_health_points(N, d):
    total_health_points = 0
    for i in range(N):
        for j in range(i+1, N):
            total_health_points += d[i] * d[j]
    return total_health_points

N = int(input())
d = list(map(int, input().split()))

result = takoyaki_festival_health_points(N, d)
print(result)
```
