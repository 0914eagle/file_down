
from math import sqrt
def calc_distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def solve():
    x, y = map(float, input().split())
    N = int(input())
    chickens = []
    for _ in range(N):
        x2, y2 = map(float, input().split())
        chickens.append((x2, y2))
    chickens.sort(key=lambda c: calc_distance(x, y, c[0], c[1]))
    total_distance = 0
    while len(chickens) > 0:
        x1, y1 = chickens.pop()
        x2, y2 = chickens.pop()
        total_distance += calc_distance(x1, y1, x2, y2)
    return total_distance

print(solve())

