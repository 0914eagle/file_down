
from math import sqrt
x1, y1, x2, y2 = map(int, input().split())
vmax, t = map(int, input().split())
vx, vy = map(int, input().split())
wx, wy = map(int, input().split())
dx = x2 - x1
dy = y2 - y1
def dist(dx, dy, vx, vy):
    return sqrt((dx - vx) ** 2 + (dy - vy) ** 2)
dt = dist(dx, dy, 0, 0) / vmax
dx = dx - vx * dt
dy = dy - vy * dt
dt += dist(dx, dy, vx, vy) / vmax
print(dt)

