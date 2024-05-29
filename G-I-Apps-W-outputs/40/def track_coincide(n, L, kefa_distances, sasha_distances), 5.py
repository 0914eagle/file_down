
def track_coincide(n, L, kefa_distances, sasha_distances):
    kefa_diffs = [kefa_distances[(i+1) % n] - kefa_distances[i] for i in range(n)]
    sasha_diffs = [sasha_distances[(i+1) % n] - sasha_distances[i] for i in range(n)]
    
    for i in range(n):
        if kefa_diffs == sasha_diffs:
            return "YES"
        kefa_diffs = [kefa_diffs[-1]] + kefa_diffs[:-1]
    
    return "NO"

# Input reading
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Check if tracks coincide
result = track_coincide(n, L, kefa_distances, sasha_distances)
print(result)
```
