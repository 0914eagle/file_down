
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())

if x3 >= x1 and x4 <= x2 and y3 >= y1 and y4 <= y2 and x5 >= x1 and x6 <= x2 and y5 >= y1 and y6 <= y2:
    print("NO")
else:
    print("YES")
