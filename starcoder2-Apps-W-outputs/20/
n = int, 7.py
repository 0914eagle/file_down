
n = int(input())
x1, y1, x2, y2 = map(int, input().split())
for i in range(n-1):
    x11, y11, x22, y22 = map(int, input().split())
    if x11 != x22 and y11 != y22:
        print("NO")
        break
    elif x11 == x22 and y11 == y22:
        print("NO")
        break
    elif x11 == x22 and y11 != y22:
        if y11 < y1:
            y1 = y11
        elif y22 > y2:
            y2 = y22
    elif x11 != x22 and y11 == y22:
        if x11 < x1:
            x1 = x11
        elif x22 > x2:
            x2 = x22
    elif x11 == x2 and y11 == y2:
        print("NO")
        break
    elif x11 == x1 and y11 == y22:
        print("NO")
        break
    elif x11 == x22 and y11 == y2:
        print("NO")
        break
    elif x11 == x2 and y11 == y1:
        print("NO")
        break
else:
    if x1 == x2 and y1 == y2:
        print("YES")
    else:
        print("NO")
