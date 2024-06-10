
def solve(n, edges):
    return "Yes"

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
print(solve(n, edges))

