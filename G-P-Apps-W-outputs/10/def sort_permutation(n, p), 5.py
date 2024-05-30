
def sort_permutation(n, p):
    swaps = []
    for i in range(n):
        if i % 2 == 0:
            j = i + 1
            if p[i] > p[j]:
                swaps.append((i + 1, j + 1))
                p[i], p[j] = p[j], p[i]
        else:
            j = i - 1
            if p[i] < p[j]:
                swaps.append((i + 1, j + 1))
                p[i], p[j] = p[j], p[i]
    
    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

# Reading input
n = int(input())
p = list(map(int, input().split()))

# Sorting the permutation
sort_permutation(n, p)
```
