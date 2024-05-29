
def min_cuts_to_build_fence(K, N, poles):
    low = 1
    high = max(poles)
    while low < high:
        mid = (low + high) // 2
        total_posts = sum(p // mid for p in poles)
        if total_posts < N:
            high = mid
        else:
            low = mid + 1
    return low - 1

# Taking input
K, N = map(int, input().split())
poles = list(map(int, input().split()))

# Calling the function and printing the result
print(min_cuts_to_build_fence(K, N, poles))
```
