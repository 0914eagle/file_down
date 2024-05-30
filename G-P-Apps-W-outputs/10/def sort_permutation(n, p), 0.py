
def sort_permutation(n, p):
    swaps = []
    def add_swap(i, j):
        swaps.append((i, j))

    for i in range(n):
        if i % 2 == 0:
            idx = p.index(n)
            if idx != n - 1:
                p[idx], p[idx + 1] = p[idx + 1], p[idx]
                add_swap(idx + 1, idx + 2)
        else:
            idx = p.index(1)
            if idx != 0:
                p[idx], p[idx - 1] = p[idx - 1], p[idx]
                add_swap(idx + 1, idx)

    return swaps

n = int(input())
p = list(map(int, input().split()))

swaps = sort_permutation(n, p)
print(len(swaps))
for i, j in swaps:
    print(i, j)
