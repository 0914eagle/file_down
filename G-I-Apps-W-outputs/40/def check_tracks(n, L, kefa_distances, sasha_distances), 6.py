
def check_tracks(n, L, kefa_distances, sasha_distances):
    def check_single_track(kefa_start, sasha_start, distances):
        normalized_distances = [(d - distances[0] + L) % L for d in distances]
        kefa_start_idx = normalized_distances.index(kefa_start)
        sasha_idx = normalized_distances.index(sasha_start)
        
        for i in range(n):
            if normalized_distances[(kefa_start_idx + i) % n] != normalized_distances[(sasha_idx + i) % n]:
                return False
        return True

    for i in range(n):
        for j in range(n):
            if check_single_track(kefa_distances[i], sasha_distances[j], kefa_distances):
                return "YES"
    
    return "NO"

n, L = map(int, input().split())
kefa_distances = list(map(int, input().split()))
sasha_distances = list(map(int, input().split()))

print(check_tracks(n, L, kefa_distances, sasha_distances))
```
