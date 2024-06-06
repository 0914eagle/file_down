
n, m = map(int, input().split())

if n == 1:
    print(m)
else:
    print((m ** n + m ** (n - 1) * (m - 1) + 1) % (10 ** 9 + 7))
