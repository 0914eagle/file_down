
for _ in range(int(input())):
    a, b, n, m = map(int, input().split())
    v, c = a, b
    while n > 0 and m > 0:
        if v > c:
            if m > 0:
                m -= 1
                c += 1
            else:
                break
        else:
            if n > 0:
                n -= 1
                v += 1
            else:
                break
    if n == 0 and m == 0:
        print("Yes")
    else:
        print("No")

