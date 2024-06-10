
import sys
input = sys.stdin.readline

def solve(n, m, h, u, c):
    pass

if __name__ == '__main__':
    n, m, h = map(int, input().split())
    u = list(map(int, input().split()))
    c = [list(map(int, input().split())) for _ in range(m)]
    ans = solve(n, m, h, u, c)
    print(ans)

