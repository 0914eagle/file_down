
a, b, l, r = [int(i) for i in input().split()]

if b < a:
    res = (r - l + 1) % (a + b)
    if res == 0 or res <= b:
        res = a
    else:
        res = b
else:
    res = (r - l + 1) % (a + b)
    if res == 0 or res <= a:
        res = a
    else:
        res = b
print(res)
