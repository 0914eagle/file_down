
def solve(n, edges):
    # Your code goes here
    return res, a, b, c

n = int(input())
edges = [tuple(map(int, input().split())) for _ in range(n - 1)]
res, a, b, c = solve(n, edges)
print(res)
print(a, b, c)

