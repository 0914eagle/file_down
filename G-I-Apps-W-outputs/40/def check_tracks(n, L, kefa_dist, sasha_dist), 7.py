
def check_tracks(n, L, kefa_dist, sasha_dist):
    for i in range(n):
        if kefa_dist == sasha_dist:
            return True
        kefa_dist = [(x + 1) % L for x in kefa_dist]
        
    return False

n, L = map(int, input().split())
kefa_dist = list(map(int, input().split()))
sasha_dist = list(map(int, input().split()))

if check_tracks(n, L, kefa_dist, sasha_dist):
    print("YES")
else:
    print("NO")
```
