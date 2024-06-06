
n, a, b, k = map(int, input().split())
s = input()

if s == '+':
    print((a ** (n + 1) - 1) // (a - 1) % (10 ** 9 + 9))
elif s == '-':
    print((b ** (n + 1) - 1) // (b - 1) % (10 ** 9 + 9))
else:
    print(0)
