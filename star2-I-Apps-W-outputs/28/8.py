
t = int(input())
a = list(map(int, input().split()))

def solve(a):
    n = len(a)
    m = 1
    while n * m != len(a):
        m += 1
    for i in range(n):
        for j in range(m):
            if a[i * m + j] == 0:
                return (n, m, i + 1, j + 1)
    return (-1,)

print(*solve(a))

