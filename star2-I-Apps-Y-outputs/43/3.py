
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
x5, y5, x6, y6 = map(int, input().split())
if x1 >= x4 or x2 <= x3 or y1 >= y4 or y2 <= y3 or x1 >= x6 or x2 <= x5 or y1 >= y6 or y2 <= y5:
    print("NO")
else:
    print("YES")

