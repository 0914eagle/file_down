
def sort_permutation(n, p):
    swaps = []
    
    def swap(i, j):
        swaps.append((i, j))
        p[i-1], p[j-1] = p[j-1], p[i-1]
    
    for i in range(n):
        if i % 2 == 0:
            # Find the maximum element in the unsorted part
            max_idx = p.index(max(p[i:]))
            if 2 * abs(i - max_idx) >= n:
                swap(i+1, max_idx+1)
        else:
            # Find the minimum element in the unsorted part
            min_idx = p.index(min(p[i:]))
            if 2 * abs(i - min_idx) >= n:
                swap(i+1, min_idx+1)
    
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

# Read input
n = int(input())
p = list(map(int, input().split()))

# Call the function with the input
sort_permutation(n, p)
```
