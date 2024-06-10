
n, a, b, c, d = map(int, input().split())
if a + b == c + d:
    print(n ** 4)
elif a + b > c + d:
    print(0)
else:
    print(n ** 4 - (n - 1) ** 4)


