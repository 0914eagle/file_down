
def check_tracks(n, L, kefa_dist, sasha_dist):
    kefa_diff = [(kefa_dist[i] - kefa_dist[0]) % L for i in range(n)]
    sasha_diff = [(sasha_dist[i] - sasha_dist[0]) % L for i in range(n)]
    
    for i in range(1, n):
        if sorted(kefa_diff) == sorted(sasha_diff):
            return "YES"
        kefa_diff = [(kefa_diff[j] + 1) % L for j in range(n)]
    
    return "NO"

# Input processing
n, L = map(int, input().split())
kefa_dist = list(map(int, input().split()))
sasha_dist = list(map(int, input().split()))

# Output
print(check_tracks(n, L, kefa_dist, sasha_dist))
```
