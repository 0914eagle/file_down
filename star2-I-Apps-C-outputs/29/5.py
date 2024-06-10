
from math import sqrt

def dist(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def is_within_sight(beacon1, beacon2, mountains):
    if dist(beacon1, beacon2) == 0:
        return True
    
    for mountain in mountains:
        if dist(beacon1, mountain) + dist(beacon2, mountain) <= mountain[2]:
            return False
        
    return True

def solve(beacons, mountains):
    n = len(beacons)
    graph = [[False for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if is_within_sight(beacons[i], beacons[j], mountains):
                graph[i][j] = True
    
    visited = [False for _ in range(n)]
    queue = [0]
    visited[0] = True
    
    while queue:
        curr = queue.pop(0)
        
        for i in range(n):
            if graph[curr][i] and not visited[i]:
                queue.append(i)
                visited[i] = True
    
    return sum(not visited[i] for i in range(n))

n, m = map(int, input().split())
beacons = [tuple(map(int, input().split())) for _ in range(n)]
mountains = [tuple(map(int, input().split())) + (r,) for _ in range(m)]

print(solve(beacons, mountains))

