
def check_coinciding_tracks(n, L, kefa_distances, sasha_distances):
    for i in range(n):
        if kefa_distances == sasha_distances:
            return "YES"
        # Rotate distances for Kefa by 1 position
        kefa_distances = [(x + 1) % L for x in kefa_distances]
    return "NO"

# Read input
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Check if Kefa and Sasha ran the coinciding tracks
result = check_coinciding_tracks(n, L, kefa_distances, sasha_distances)
print(result)
```
