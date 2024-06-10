
def solve(n, m, h, u, c):
    return 0

if __name__ == '__main__':
    n, m, h = map(int, input().split())
    u = list(map(int, input().split()))
    c = [list(map(int, input().split())) for _ in range(m)]
    print(solve(n, m, h, u, c))

