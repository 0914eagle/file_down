
for _ in range(int(input())):
    a, b, n, m = map(int, input().split())
    v = a
    c = b
    ok = True
    while n > 0 and m > 0:
        if v > c:
            if a == 0:
                ok = False
                break
            a -= 1
        else:
            if b == 0:
                ok = False
                break
            b -= 1
        n -= 1
        m -= 1
    while n > 0:
        if v > c:
            if a == 0:
                ok = False
                break
            a -= 1
        else:
            if b == 0:
                ok = False
                break
            b -= 1
        n -= 1
    while m > 0:
        if v > c:
            if b == 0:
                ok = False
                break
            b -= 1
        else:
            if a == 0:
                ok = False
                break
            a -= 1
        m -= 1
    if ok:
        print("Yes")
    else:
        print("No")

