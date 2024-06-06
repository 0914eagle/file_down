
def bfs(start, graph):
    que = []
    que.append(start)
    while len(que):
        now = que.pop(0)
        for i in graph[now]:
            if i[1] == -1:
                i[1] = now
                que.append(i[0])
            if i[0] == end:
                return i[1]
    return -1

def bfs_1(start, graph):
    que = []
    que.append(start)
    while len(que):
        now = que.pop(0)
        for i in graph[now]:
            if i[1] == -1:
                i[1] = now
                que.append(i[0])
            if i[0] == end:
                return i[1]
    return -1

if __name__ == '__main__':
    n = int(input())
    graph = {}
    graph_1 = {}
    for i in range(1, n+1):
        graph[i] = []
        graph_1[i] = []
    for i in range(1, n+1):
        a = list(map(int, input().split()))
        for j in range(4):
            if a[j] != 0:
                graph[i].append([a[j], -1])
                graph_1[i].append([a[j], -1])
    for i in range(1, n+1):
        a = list(map(int, input().split()))
        for j in range(4):
            if a[j] != 0:
                graph_1[i].append([a[j], -1])
    start = 1
    end = n
    print(bfs(start, graph))
    print(bfs_1(start, graph_1))

