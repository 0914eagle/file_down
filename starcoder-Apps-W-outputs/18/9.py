
def bfs(room):
    visited[room] = 1
    if room == n:
        print('Yes')
        exit()
    for next_room in room_graph[room]:
        if next_room and not visited[next_room]:
            bfs(next_room)

n = int(input())
room_graph = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for i in range(1, n + 1):
    exits = list(map(int, input().split()))
    room_graph[i] = exits

bfs(1)

print('No')
