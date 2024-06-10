
def solve(n, C, p, b, u):
    return 0

if __name__ == '__main__':
    n, C = map(int, input().split())
    p = [0] * n
    b = [0] * n
    u = [0] * n
    for i in range(n):
        p[i], b[i], u[i] = map(int, input().split())
    print(solve(n, C, p, b, u))

