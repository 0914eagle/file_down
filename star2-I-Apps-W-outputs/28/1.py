
t = int(input())
a = list(map(int, input().split()))

def find_matrix(a):
    n = len(a)
    m = 1
    while n * m != len(a):
        m += 1
        n = len(a) // m
    dist = [0] * n
    for i in range(n):
        dist[i] = abs(i - a.index(0))
    x = dist.index(max(dist))
    y = a.index(max(dist)) - x
    return n, m, x + 1, y + 1

n, m, x, y = find_matrix(a)
if n * m != len(a):
    print(-1)
else:
    print(n, m)
    print(x, y)

