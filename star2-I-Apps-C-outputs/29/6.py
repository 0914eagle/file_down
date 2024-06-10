
import math

def solve(beacons, peaks):
    graph = [[False for _ in range(len(beacons))] for _ in range(len(beacons))]
    for i in range(len(beacons)):
        for j in range(i + 1, len(beacons)):
            blocked = False
            for peak in peaks:
                if math.sqrt((beacons[i][0] - peak[0]) ** 2 + (beacons[i][1] - peak[1]) ** 2) + math.sqrt((beacons[j][0] - peak[0]) ** 2 + (beacons[j][1] - peak[1]) ** 2) <= 2 * peak[2]:
                    blocked = True
                    break
            if not blocked:
                graph[i][j] = graph[j][i] = True
    visited = [False for _ in range(len(beacons))]
    queue = [0]
    visited[0] = True
    while queue:
        curr = queue.pop(0)
        for i in range(len(beacons)):
            if graph[curr][i] and not visited[i]:
                queue.append(i)
                visited[i] = True
    return sum(not v for v in visited)

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
peaks = [tuple(map(int, input().split()) + (int(input()),)) for _ in range(m)]
print(solve(beacons, peaks))

