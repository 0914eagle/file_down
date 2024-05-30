
def sort_permutation(n, p):
    swaps = []
    for i in range(n // 2):
        if p[i] > n // 2:
            swaps.append((i + 1, p.index(n // 2 + 1) + 1))
            p[i], p[p.index(n // 2 + 1)] = p[p.index(n // 2 + 1)], p[i]

        if p[i + n // 2] <= n // 2:
            swaps.append((i + n // 2 + 1, p.index(n // 2 + 1) + 1))
            p[i + n // 2], p[p.index(n // 2 + 1)] = p[p.index(n // 2 + 1)], p[i + n // 2]

    print(len(swaps))
    for swap in swaps:
        print(swap[0], swap[1])

# Input
n = int(input())
p = list(map(int, input().split()))

# Function call
sort_permutation(n, p)
```
