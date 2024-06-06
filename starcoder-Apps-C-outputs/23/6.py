
from itertools import product
from collections import deque
from math import cos, sin, pi, sqrt

def walk(map_, x, y, low, high, a):
    map_[x][y] = 0
    q = deque([(x, y, 0)])
    while q:
        x, y, t = q.popleft()
        for dx, dy in product([-1, 1, 0, 0], [0, 0, -1, 1]):
            x_, y_ = x+dx, y+dy
            if 0 <= x_ < W and 0 <= y_ < H and map_[x_][y_] == 1:
                h1 = max(0, map_heights[y][x]+a*cos(t*2*pi/12)-1)
                h2 = max(0, map_heights[y_][x_]+a*cos((t+m/1000)*2*pi/12)-1)
                if abs(h1-h2) <= 1 and h1 >= low and h2 >= low and h1 <= high and h2 <= high:
                    map_[x_][y_] = 0
                    q.append((x_, y_, t+m/1000))
    return map_

def distance(x1, y1, x2, y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)*10

if __name__ == '__main__':
    a, m = map(float, input().split())
    W, H, X, Y = map(int, input().split())
    map_heights = [list(map(int, input().split())) for _ in range(H)]
    map_ = [[1]*W for _ in range(H)]
    walk(map_, X, Y, 0, 1000, a)
    walk(map_, X, Y, 1000, 2000, a)
    print(max(distance(X, Y, x, y) for x, y in product(range(W), range(H)) if map_[y][x] == 0))
