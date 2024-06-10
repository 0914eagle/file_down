
import math

roost_x, roost_y = map(float, input().split())
N = int(input())

hiding_spots = []
for _ in range(N):
  x, y = map(float, input().split())
  hiding_spots.append((x, y))

hiding_spots.sort(key=lambda h: math.sqrt((h[0] - roost_x)**2 + (h[1] - roost_y)**2))

hen1 = hen2 = None
distance = 0
for x, y in hiding_spots:
  if hen1 is None:
    hen1 = (x, y)
  elif hen2 is None:
    hen2 = (x, y)
  else:
    distance += math.sqrt((hen1[0] - hen2[0])**2 + (hen1[1] - hen2[1])**2)
    hen1 = hen2
    hen2 = (x, y)

if hen1 is not None:
  distance += math.sqrt((hen1[0] - roost_x)**2 + (hen1[1] - roost_y)**2)

print(distance)

