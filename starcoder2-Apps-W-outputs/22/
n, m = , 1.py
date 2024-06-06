
n, m = map(int, input().split())

if n == 1:
    print(m)
elif n == 2:
    print(m * (m + 1))
elif n == 3:
    print(m * (m + 1) * (m + 2) - (m - 1) * (m - 2) * (m - 3))
else:
    print(m * (m + 1) * (m + 2) * (m + 3))
