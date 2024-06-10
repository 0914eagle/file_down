
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)

x1, y1, x2, y2 = map(int, input().split())
vmax, t = map(int, input().split())
vx, vy = map(int, input().split())
wx, wy = map(int, input().split())
distance1 = distance(x1, y1, x2, y2)
distance2 = distance(vx, vy, wx, wy)

if distance2 == 0:
    print(distance1 / vmax)
else:
    time1 = distance1 / vmax
    time2 = distance1 / (vmax - distance2)
    print(time1 + time2)

