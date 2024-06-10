
def solve(n, q, painters):
    pass

n, q = map(int, input().split())
painters = [list(map(int, input().split())) for _ in range(q)]
print(solve(n, q, painters))

