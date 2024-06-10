
import math

def distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def is_in_sight(beacon_a, beacon_b, mountains):
    for mountain in mountains:
        if distance(beacon_a, mountain) < mountain[2] and distance(beacon_b, mountain) < mountain[2]:
            return False
    return True

def solve(beacons, mountains):
    graph = [[False for _ in range(len(beacons))] for _ in range(len(beacons))]
    for i in range(len(beacons)):
        for j in range(i + 1, len(beacons)):
            if is_in_sight(beacons[i], beacons[j], mountains):
                graph[i][j] = True
                graph[j][i] = True
    visited = [False for _ in range(len(beacons))]
    queue = [0]
    visited[0] = True
    while queue:
        current = queue.pop(0)
        for i in range(len(beacons)):
            if graph[current][i] and not visited[i]:
                queue.append(i)
                visited[i] = True
    return sum(not visited[i] for i in range(len(beacons)))

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
mountains = [tuple(map(int, input().split())) + (r,) for r in map(int, input().split())]
print(solve(beacons, mountains))

