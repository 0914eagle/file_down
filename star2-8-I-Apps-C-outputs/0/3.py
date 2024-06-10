
import math

def find_distance(x1, y1, x2, y2):
  return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def find_time_to_destination(x1, y1, x2, y2, vmax, t, v1x, v1y, v2x, v2y):
  dist_to_destination = find_distance(x1, y1, x2, y2)
  total_time = 0
  if dist_to_destination <= vmax * t:
    total_time += dist_to_destination / vmax
  else:
    total_time += t
    dist_to_destination -= vmax * t
    total_time += dist_to_destination / math.sqrt(vmax ** 2 - (v1x ** 2 + v1y ** 2))

  return total_time
x1, y1, x2, y2 = map(int, input().split())
vmax, t = map(int, input().split())
v1x, v1y = map(int, input().split())
v2x, v2y = map(int, input().split())

print(find_time_to_destination(x1, y1, x2, y2, vmax, t, v1x, v1y, v2x, v2y))

