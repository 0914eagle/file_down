
def solve(t, a):
    n = 1
    m = t
    while n * m != t:
        n += 1
        m = t // n
    dist = [0] * t
    for i in range(n):
        for j in range(m):
            dist[i * m + j] = abs(i - n // 2) + abs(j - m // 2)
    for i in range(n):
        for j in range(m):
            if dist[i * m + j] == 0:
                x = i + 1
                y = j + 1
    for i in range(n):
        for j in range(m):
            if dist[i * m + j] != a[i * m + j]:
                return -1
    return n, m, x, y

t = int(input())
a = list(map(int, input().split()))
n, m, x, y = solve(t, a)
if n == -1:
    print(n)
else:
    print(n, m)
    print(x, y)

