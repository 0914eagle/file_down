
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    white = (x2 - x1 + 1) * (y2 - y1 + 1)
    black = (x4 - x3 + 1) * (y4 - y3 + 1)
    print(white, black)

