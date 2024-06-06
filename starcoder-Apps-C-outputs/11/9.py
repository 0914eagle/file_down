
h, m, s, t1, t2 = map(int, input().split())
if t1 < t2:
    if m == 0 and s == 0:
        print("YES")
    else:
        print("NO")
else:
    if m == 59 and s == 45:
        print("NO")
    else:
        print("YES")
