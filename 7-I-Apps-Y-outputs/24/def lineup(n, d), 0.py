
def lineup(n, d):
    d.insert(0, 0)
    d.append(n-1)
    for i in range(1, n):
        d[i] += d[i-1]
    for i in range(n-1, -1, -1):
        print(d[i], end=' ')

n = int(input())
d = list(map(int, input().split()))
lineup(n, d)

