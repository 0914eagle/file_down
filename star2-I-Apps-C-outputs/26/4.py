
def solve(n, m, roads):
    return 0

n, m = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(n, m, roads))

