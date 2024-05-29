
def check_coinciding_tracks(n, L, kefa_distances, sasha_distances):
    kefa_barriers = [0] * L
    sasha_barriers = [0] * L
    
    for i in range(n):
        kefa_pos = kefa_distances[i]
        sasha_pos = sasha_distances[i]
        
        kefa_barriers[kefa_pos] += 1
        sasha_barriers[sasha_pos] += 1
    
    if kefa_barriers == sasha_barriers:
        return "YES"
    else:
        return "NO"

# Input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Output
print(check_coinciding_tracks(n, L, kefa_distances, sasha_distances))
```
