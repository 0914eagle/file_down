
from math import sqrt

x1, y1, x2, y2 = map(int, input().split())
vmax, t = map(int, input().split())
vx, vy = map(int, input().split())
wx, wy = map(int, input().split())
dx = x2 - x1
dy = y2 - y1

def distance(x, y):
  return sqrt(x**2 + y**2)

dist = distance(dx, dy)
time = dist / vmax

def dot_product(x1, y1, x2, y2):
  return x1 * x2 + y1 * y2

def cross_product(x1, y1, x2, y2):
  return x1 * y2 - x2 * y1

v_dist = distance(vx, vy)
w_dist = distance(wx, wy)

v_angle = dot_product(dx, dy, vx, vy) / (dist * v_dist)
w_angle = dot_product(dx, dy, wx, wy) / (dist * w_dist)

v_angle = cross_product(dx, dy, vx, vy) / (dist * v_dist)
w_angle = cross_product(dx, dy, wx, wy) / (dist * w_dist)

if v_angle > 0:
  time += v_dist / vmax
if w_angle > 0:
  time += w_dist / vmax

print(time)

