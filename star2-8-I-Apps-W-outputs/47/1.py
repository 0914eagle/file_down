

n, a, b, c, d = map(int, input().split())
if n == 1:
    print(0 if a != b or b != c or c != d else 1)
else:
    print((n - 1) ** 4 + (n - 1) ** 2)


