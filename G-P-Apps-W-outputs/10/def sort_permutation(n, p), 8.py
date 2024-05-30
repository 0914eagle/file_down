
def sort_permutation(n, p):
    swaps = []
    for i in range(n-1):
        if p[i] > p[i+1]:
            idx = p.index(i+1)
            if abs(idx - i) * 2 >= n:
                swaps.append((i+1, idx+1))
                p[i], p[idx] = p[idx], p[i]
    print(len(swaps))
    for swap in swaps:
        print(*swap)

# Input parsing
n = int(input())
p = list(map(int, input().split()))

# Call the function
sort_permutation(n, p)
```
