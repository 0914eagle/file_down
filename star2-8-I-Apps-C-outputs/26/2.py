
def solve(n, m, a, w):
    return [0] * n

n, m = map(int, input().split())
a = list(map(int, input().split()))
w = list(map(int, input().split()))
ans = solve(n, m, a, w)
print(*ans)

