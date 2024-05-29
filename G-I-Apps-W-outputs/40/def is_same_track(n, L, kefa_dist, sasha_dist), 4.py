
def is_same_track(n, L, kefa_dist, sasha_dist):
    # Rotate the distances to check if Kefa and Sasha ran the same track
    for i in range(len(kefa_dist)):
        rotated_kefa_dist = [(x + i) % L for x in kefa_dist]
        if rotated_kefa_dist == sasha_dist:
            return "YES"
    
    return "NO"

# Input
n, L = map(int, input().split())
kefa_dist = list(map(int, input().split()))
sasha_dist = list(map(int, input().split()))

# Output
print(is_same_track(n, L, kefa_dist, sasha_dist))
```
