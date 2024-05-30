
def solve(b, d, c, l):
    if b+d+c != l:
        print("impossible")
        return
    if b == 0 and d == 0 and c == 0:
        print("0 0 0")
        return
    if b == 0 and d == 0 and c > 0:
        print("0 0", c)
        return
    if b == 0 and c == 0 and d > 0:
        print("0", d, "0")
        return
    if c == 0 and b == 0 and d > 0:
        print(d, "0 0")
        return
    if d == 0 and c == 0 and b > 0:
        print("0", b, "0")
        return
    if b == 0 and d > 0 and c > 0:
        print("0", d, c)
        return
    if c == 0 and b > 0 and d > 0:
        print(b, d, "0")
        return
    if d == 0 and b > 0 and c > 0:
        print(b, "0", c)
        return
    if b > 0 and c > 0 and d > 0:
        print(b, d, c)
        return
    else:
        print("impossible")
        return

