
def solve(n, m, a, b):
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    a, b = [], []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    print(solve(n, m, a, b))

