
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def solve(x, y, spots):
    spots.sort(key=lambda s: distance(x, y, s[0], s[1]))
    used = 0
    result = 0
    for spot in spots:
        if used == 2:
            result += distance(x, y, spot[0], spot[1])
            used = 1
        else:
            result += distance(x, y, spot[0], spot[1])
            used += 1
    return result

x, y = map(float, input().split())
n = int(input())
spots = []
for _ in range(n):
    spots.append(tuple(map(float, input().split())))
print(solve(x, y, spots))

