
def solve(n, k, graph, disqualified):
    return 0

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
disqualified = list(map(int, input().split()))
print(solve(n, k, graph, disqualified))

