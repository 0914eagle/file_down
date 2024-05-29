
def check_coinciding_tracks(n, L, kefa_distances, sasha_distances):
    # Generate all possible rotations of Sasha's distances
    for i in range(n):
        rotated_sasha = sasha_distances[i:] + sasha_distances[:i]
        
        # Check if the rotations match Kefa's distances
        if kefa_distances == rotated_sasha:
            return "YES"
    
    return "NO"

# Input parsing
n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

# Check if tracks coincide
result = check_coinciding_tracks(n, L, kefa_distances, sasha_distances)
print(result)
```
