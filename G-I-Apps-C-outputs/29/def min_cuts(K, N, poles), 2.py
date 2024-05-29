
def min_cuts(K, N, poles):
    max_length = max(poles)
    cuts = 0
    while max_length % N != 0:
        cuts += 1
        max_length -= 1
    
    return cuts

# Input
K, N = map(int, input().split())
poles = list(map(int, input().split()))

# Output
print(min_cuts(K, N, poles))
```
