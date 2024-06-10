
import math

def is_in_sight(beacon1, beacon2, mountains):
    dx = beacon2[0] - beacon1[0]
    dy = beacon2[1] - beacon1[1]
    dist = math.sqrt(dx * dx + dy * dy)
    for mountain in mountains:
        if math.sqrt((beacon1[0] - mountain[0]) * (beacon1[0] - mountain[0]) + (beacon1[1] - mountain[1]) * (beacon1[1] - mountain[1])) + mountain[2] >= dist:
            return True
    return False

def solve(beacons, mountains):
    n = len(beacons)
    graph = [[False for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if is_in_sight(beacons[i], beacons[j], mountains):
                graph[i][j] = True
                graph[j][i] = True
    visited = [False for _ in range(n)]
    queue = [0]
    visited[0] = True
    while queue:
        curr = queue.pop(0)
        for i in range(n):
            if graph[curr][i] and not visited[i]:
                queue.append(i)
                visited[i] = True
    return sum(not v for v in visited)

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
mountains = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(beacons, mountains))

