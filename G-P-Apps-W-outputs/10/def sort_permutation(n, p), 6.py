
def sort_permutation(n, p):
    swaps = []
    for i in range(n):
        if i % 2 == 0:
            swaps.append((i, p.index(i+1)))
        else:
            swaps.append((i, p.index(i+1, i)))
        p[i], p[swaps[-1][1]] = p[swaps[-1][1]], p[i]

    print(len(swaps))
    for swap in swaps:
        print(swap[0]+1, swap[1]+1)

# Read input
n = int(input())
p = list(map(int, input().split()))

# Solve the problem
sort_permutation(n, p)
```
