
def takoyaki_festival_health_points(N, deliciousness):
    total_points = 0
    for i in range(N):
        for j in range(i+1, N):
            total_points += deliciousness[i] * deliciousness[j]
    
    return total_points

# Input reading
N = int(input())
deliciousness = list(map(int, input().split()))

# Calculate and print the result
print(takoyaki_festival_health_points(N, deliciousness))
```
