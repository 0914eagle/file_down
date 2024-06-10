
a, b = map(int, input().split())
c, d = map(int, input().split())
det = a * d - b * c
if det == 0:
    print(min(abs(a - c), abs(b - d)))
else:
    print(0)

