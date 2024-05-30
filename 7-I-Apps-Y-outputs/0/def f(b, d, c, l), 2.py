
def f(b, d, c, l):
    if l == 0:
        return
    if b > 0 and l >= b:
        f(b-1, d, c, l-b)
        print(b, d, c)
    if c > 0 and l >= c:
        f(b, d, c-1, l-c)
        print(b, d, c)
    if d > 0 and l >= d:
        f(b, d-1, c, l-d)
        print(b, d, c)

