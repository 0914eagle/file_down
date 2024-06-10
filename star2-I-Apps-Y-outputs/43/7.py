
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

if (x1 < x3 < x2 or x1 < x4 < x2) and (y1 < y3 < y2 or y1 < y4 < y2):
    print("NO")
elif (x1 < x5 < x2 or x1 < x6 < x2) and (y1 < y5 < y2 or y1 < y6 < y2):
    print("NO")
else:
    print("YES")

