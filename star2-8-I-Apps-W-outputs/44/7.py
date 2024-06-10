

n, m = map(int, input().split())
a = list(map(int, input().split()))
swaps = [tuple(map(int, input().split())) for _ in range(m)]

for i in range(m):
    pos1, pos2 = swaps[i]
    temp = a[pos1 - 1]
    a[pos1 - 1] = a[pos2 - 1]
    a[pos2 - 1] = temp

print(' '.join(map(str, a)))

