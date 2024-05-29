
# Python function to solve the takoyaki festival problem

def takoyaki_festival(N, deliciousness):
    total_health_points = 0
    for i in range(N):
        for j in range(i+1, N):
            total_health_points += deliciousness[i] * deliciousness[j]
    return total_health_points

# Input
N = int(input())
deliciousness = list(map(int, input().split()))

# Output
print(takoyaki_festival(N, deliciousness))
```
