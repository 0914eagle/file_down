
def solve(r, c, k, l, x0, y0, t):
    pass

if __name__ == '__main__':
    r, c, k, l = map(int, input().split())
    x0, y0 = map(int, input().split())
    t = [list(map(int, input().split())) for _ in range(r)]
    print(solve(r, c, k, l, x0, y0, t))

