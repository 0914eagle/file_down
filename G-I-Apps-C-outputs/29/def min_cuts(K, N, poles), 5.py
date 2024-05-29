
def min_cuts(K, N, poles):
    low = 1
    high = max(poles)
    
    while low < high:
        mid = (low + high + 1) // 2
        pieces = sum(pole // mid for pole in poles)
        if pieces < N:
            high = mid - 1
        else:
            low = mid
            
    return sum(pole // low for pole in poles) - N

# Read input
K, N = map(int, input().split())
poles = list(map(int, input().split()))

# Call the function and print the result
print(min_cuts(K, N, poles))
```
