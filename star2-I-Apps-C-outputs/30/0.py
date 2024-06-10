
def solve(n, a, b):
    pass

if __name__ == "__main__":
    n = int(input())
    a = []
    b = []
    for _ in range(n):
        x, y = map(int, input().split())
        a.append(x)
        b.append(y)
    print(solve(n, a, b))

