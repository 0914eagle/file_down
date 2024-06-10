
def solve(n, m, x1, y1, x2, y2, x3, y3, x4, y4):
    white = (x2 - x1 + 1) * (y2 - y1 + 1)
    black = (x4 - x3 + 1) * (y4 - y3 + 1)
    overlap = max(min(x2, x4) - max(x1, x3) + 1, 0) * max(min(y2, y4) - max(y1, y3) + 1, 0)
    return white - overlap, black - overlap

for _ in range(int(input())):
    n, m = map(int, input().split())
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())
    white, black = solve(n, m, x1, y1, x2, y2, x3, y3, x4, y4)
    print(white, black)

