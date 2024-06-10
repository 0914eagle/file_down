
def solve(n, a):
    balls = [i for i in range(1, n + 1) if a[i - 1]]
    return len(balls), balls


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    m, balls = solve(n, a)
    print(m)
    print(*balls)

