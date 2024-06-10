
def solve(n, a, b):
    pass

if __name__ == '__main__':
    n = int(input())
    a = [0] * n
    b = [0] * n
    for i in range(n):
        a[i], b[i] = map(int, input().split())
    print(solve(n, a, b))

