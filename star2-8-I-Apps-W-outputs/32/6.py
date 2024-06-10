
t = int(input())
for _ in range(t):
    a, b, n, m = map(int, input().split())
    v = a
    c = b
    for _ in range(n + m):
        if v > c:
            if m > 0:
                c += 1
                m -= 1
            else:
                print("No")
                break
        else:
            if n > 0:
                v += 1
                n -= 1
            else:
                print("No")
                break
    else:
        print("Yes")

