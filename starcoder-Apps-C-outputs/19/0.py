
from collections import deque
def make_graph(times):
    graph = {}
    for time in times:
        graph[time] = []
        t_l = list(time)
        for i in range(4):
            t_l[i] = str(int(t_l[i]) + 1) if int(t_l[i]) < 9 else '0'
            new_t = ''.join(t_l)
            graph[time].append(new_t)
            t_l = list(time)
            t_l[i] = str(int(t_l[i]) - 1) if int(t_l[i]) > 0 else '9'
            new_t = ''.join(t_l)
            graph[time].append(new_t)
            t_l = list(time)
    return graph
def BFS(graph, start):
    seen = []
    queue = deque([start])
    while queue:
        curr = queue.popleft()
        if curr not in seen:
            seen.append(curr)
            for neighbor in graph[curr]:
                queue.append(neighbor)
    return seen
def test_time(t):
    return t[:2] <= '23' and t[2:] <= '59'

times = []
for _ in range(2):
    time = input()
    times.append(time)

times = set(times)
graph = make_graph(times)

seen = BFS(graph, times.pop())

for time in seen:
    if test_time(time):
        times.add(time)

times = list(times)
times.sort()
print(len(times))
for time in times:
    print(time)
