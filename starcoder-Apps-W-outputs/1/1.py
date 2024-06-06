
n, m = map(int, input().split())
p = list(map(int, input().split()))
s = []
for i in range(m):
    s.append(map(int, input().split()))

def make_graph(s):
    graph = [[] for _ in range(n)]
    for i, j in s:
        graph[i-1].append(j-1)
        graph[j-1].append(i-1)
    return graph

def bfs(s, start):
    seen, queue = set([start]), collections.deque([start])
    while queue:
        vertex = queue.popleft()
        for node in graph[vertex]:
            if node not in seen:
                seen.add(node)
                queue.append(node)
    return seen

graph = make_graph(s)

for i in range(n):
    if len(bfs(graph, i)) == n:
        print('Yes')
        exit()

print('No')
