
from math import sqrt

def dist(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)

def is_visible(beacon1, beacon2, mountains):
    x1, y1 = beacon1
    x2, y2 = beacon2
    for x, y, r in mountains:
        if dist(x1, y1, x, y) + dist(x2, y2, x, y) < r:
            return False
    return True

def solve(beacons, mountains):
    n = len(beacons)
    adj = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(i + 1, n):
            if is_visible(beacons[i], beacons[j], mountains):
                adj[i][j] = adj[j][i] = True
    visited = [False] * n
    queue = [0]
    visited[0] = True
    while queue:
        curr = queue.pop(0)
        for i in range(n):
            if adj[curr][i] and not visited[i]:
                visited[i] = True
                queue.append(i)
    return sum(not v for v in visited)

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
mountains = [tuple(map(int, input().split())) for _ in range(m)]
print(solve(beacons, mountains))

