
def solve(n, m, x1, y1, x2, y2, x3, y3, x4, y4):
    white = (x2 - x1 + 1) * (y2 - y1 + 1)
    black = (x4 - x3 + 1) * (y4 - y3 + 1)
    if x1 <= x3 <= x2 and y1 <= y3 <= y2:
        white -= (x3 - x1 + 1) * (y3 - y1 + 1)
    if x1 <= x4 <= x2 and y1 <= y4 <= y2:
        black -= (x4 - x1 + 1) * (y4 - y1 + 1)
    return white, black


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        x1, y1, x2, y2 = map(int, input().split())
        x3, y3, x4, y4 = map(int, input().split())
        white, black = solve(n, m, x1, y1, x2, y2, x3, y3, x4, y4)
        print(white, black)

