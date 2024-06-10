
import math
def dist(x1, y1, x2, y2):
  return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
x1, y1, x2, y2 = map(int, input().split())
vmax, t = map(int, input().split())
vx, vy = map(int, input().split())
wx, wy = map(int, input().split())
d = dist(x1, y1, x2, y2)
if d <= vmax * t:
  print(d / vmax)
else:
  d1 = dist(x1, y1, x1 + vx * t, y1 + vy * t)
  d2 = dist(x1 + vx * t, y1 + vy * t, x2, y2)
  print((d1 + d2) / vmax)

