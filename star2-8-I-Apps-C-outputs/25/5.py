
n, m, k = map(int, input().split())
ores = list(map(int, input().split()))
coals = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]
for _ in range(n):
    row = list(map(int, input().split()))
    for i in range(1, row[0] + 1):
        graph[row[i]].append(_ + 1)
visited = [False] * (n + 1)
visited[1] = True
queue = [1]
while queue:
    curr = queue.pop(0)
    for node in graph[curr]:
        if not visited[node]:
            visited[node] = True
            queue.append(node)
for ore in ores:
    if not visited[ore]:
        print("impossible")
        exit(0)
for coal in coals:
    if not visited[coal]:
        print("impossible")
        exit(0)
print(len(ores) + len(coals) - 1)

