
def solve(n, m, d, a, b):
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    d = list(map(int, input().split()))
    a = [0] * m
    b = [0] * m
    for i in range(m):
        a[i], b[i] = map(int, input().split())
    ans = solve(n, m, d, a, b)
    for x in ans:
        print(x)

