
a, b, l, r = map(int, input().split())
n = (r - l) // (a + b)
n2 = n * (a + b)
if l > n2 + b:
    print(b)
elif l > n2:
    print(r - l + 1)
elif r <= n2:
    print(a)
else:
    print(a - (n2 + b - l) + 1)
