
import math

def distance(tower1, tower2):
    return math.sqrt((tower1[0] - tower2[0])**2 + (tower1[1] - tower2[1])**2)

def max_towers_within_connected_region(n, towers):
    max_towers = 0
    for i in range(n):
        for j in range(i+1, n):
            dist = distance(towers[i], towers[j])
            if dist <= 2:
                max_towers = max(max_towers, n + 1)
            else:
                count = 0
                for k in range(n):
                    if distance(towers[i], towers[k]) <= 2 or distance(towers[j], towers[k]) <= 2:
                        count += 1
                max_towers = max(max_towers, count)
    return max_towers

n = int(input())
towers = []
for _ in range(n):
    x, y = map(float, input().split())
    towers.append((x, y))

result = max_towers_within_connected_region(n, towers)
print(result)
