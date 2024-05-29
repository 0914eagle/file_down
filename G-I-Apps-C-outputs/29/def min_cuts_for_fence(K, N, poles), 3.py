
def min_cuts_for_fence(K, N, poles):
    max_len = max(poles)
    cuts = 0
    for pole_len in poles:
        cuts += (max_len // pole_len) - 1
    return cuts

# Input
K, N = map(int, input().split())
poles = list(map(int, input().split()))

# Output
print(min_cuts_for_fence(K, N, poles))
```
