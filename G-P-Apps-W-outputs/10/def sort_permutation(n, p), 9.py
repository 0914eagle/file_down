
def sort_permutation(n, p):
    swaps = []
    for i in range(n):
        if i % 2 == 0:
            idx = p.index(n - i // 2)
        else:
            idx = p.index(i // 2 + 1)
        if idx != n - 1 - i:
            p[idx], p[n - 1 - i] = p[n - 1 - i], p[idx]
            swaps.append((idx + 1, n - i))
    return swaps

n = int(input())
p = list(map(int, input().split()))

result = sort_permutation(n, p)

print(len(result))
for swap in result:
    print(swap[0], swap[1])
