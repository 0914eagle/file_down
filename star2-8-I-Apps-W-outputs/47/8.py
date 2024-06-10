
n, a, b, c, d = map(int, input().split())
if a == b and b == c and c == d:
    print(n ** 4)
elif a == c and b == d:
    print(n ** 3 * (n - 1))
elif a == b and c == d:
    print(n ** 3 * (n - 1))
elif a == d and b == c:
    print(n ** 3 * (n - 1))
else:
    print(0)

