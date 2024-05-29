
def min_cuts_for_fence(K, N, poles):
    # Sort the poles in descending order
    poles.sort(reverse=True)
    
    # Initialize the number of cuts required
    cuts = 0
    
    for i in range(1, K):
        diff = poles[i-1] - poles[i]
        if diff > 0:
            cuts += diff
    
    return cuts

# Input
K, N = map(int, input().split())
poles = list(map(int, input().split()))

# Output
print(min_cuts_for_fence(K, N, poles))
```
