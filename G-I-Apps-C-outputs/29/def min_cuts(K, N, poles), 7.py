
def min_cuts(K, N, poles):
    max_length = max(poles)
    cuts = 0
    for pole in poles:
        cuts += (pole // max_length)
    return cuts

# Input
K, N = map(int, input().split())
poles = list(map(int, input().split()))

# Output
print(min_cuts(K, N, poles))
```
