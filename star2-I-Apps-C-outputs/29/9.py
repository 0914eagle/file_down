
import math

def is_in_sight(beacon1, beacon2, mountains):
    dx = beacon2[0] - beacon1[0]
    dy = beacon2[1] - beacon1[1]
    distance = math.sqrt(dx*dx + dy*dy)
    
    for mountain in mountains:
        dx = mountain[0] - beacon1[0]
        dy = mountain[1] - beacon1[1]
        distance_to_mountain = math.sqrt(dx*dx + dy*dy)
        
        if distance_to_mountain < mountain[2]:
            return False
        
    return True
    
def solve(beacons, mountains):
    n = len(beacons)
    
    graph = [[False for i in range(n)] for j in range(n)]
    
    for i in range(n):
        for j in range(i+1, n):
            if is_in_sight(beacons[i], beacons[j], mountains):
                graph[i][j] = True
                graph[j][i] = True
    
    visited = [False for i in range(n)]
    
    queue = [0]
    
    while queue:
        curr = queue.pop(0)
        
        if not visited[curr]:
            visited[curr] = True
            
            for i in range(n):
                if graph[curr][i] and not visited[i]:
                    queue.append(i)
    
    return sum(not v for v in visited)
    
n, m = map(int, input().split())

beacons = []
mountains = []

for i in range(n):
    x, y = map(int, input().split())
    
    beacons.append((x, y))
    
for i in range(m):
    x, y, r = map(int, input().split())
    
    mountains.append((x, y, r))
    
print(solve(beacons, mountains))

