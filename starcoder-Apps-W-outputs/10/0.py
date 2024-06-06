
a, b, c, d, e, f = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = int(e)
f = int(f)
if (a + b + f == d + e + c) or (a + b + e == d + f + c) or (a + b + d == f + e + c) or (a + c + d == f + e + b) or (a + c + f == d + e + b) or (a + c + e == d + f + b) or (a + d + f == b + e + c) or (a + d + e == b + f + c) or (a + e + f == b + c + d):
    print("YES")
else:
    print("NO")
