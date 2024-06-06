
t = int(input())
data = []
for i in range(t):
    data.append([])
    n = int(input())
    for j in range(n):
        d = list(map(int, input().split()))
        data[i].append(d)

visited = []
for i in range(t):
    visited.append(0)

def solve(node, data, visited):
    if visited[node] == 1:
        return 0
    visited[node] = 1
    minn = 100000000
    for d in data[node][1:]:
        x = solve(d, data, visited) + data[node][0]
        minn = min(x, minn)
    return minn

print(solve(0, data, visited))

