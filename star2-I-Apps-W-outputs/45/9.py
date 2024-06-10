
def solve(n, m, a, b):
    pass

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    print(solve(n, m, a, b))

