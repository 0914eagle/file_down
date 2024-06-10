
def solve(n, m, x1, y1, x2, y2, x3, y3, x4, y4):
    w = (x2 - x1 + 1) * (y2 - y1 + 1)
    b = (x4 - x3 + 1) * (y4 - y3 + 1)
    w -= b
    return w, b

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    w, b = solve(n, m, x1, y1, x2, y2, x3, y3, x4, y4)
    print(w, b)

