
from math import sqrt
def distance(x1, y1, x2, y2):
  return sqrt((x1 - x2)**2 + (y1 - y2)**2)
def solve(fox, hens):
  hiding_spots = [(float(input()), float(input())) for _ in range(int(input()))]
  min_distance = float('inf')
  for i in range(len(hiding_spots)):
    for j in range(i + 1, len(hiding_spots)):
      distance_to_hiding_spots = distance(fox[0], fox[1], hiding_spots[i][0], hiding_spots[i][1]) + distance(fox[0], fox[1], hiding_spots[j][0], hiding_spots[j][1])
      min_distance = min(min_distance, distance_to_hiding_spots)
  return min_distance

fox = (float(input()), float(input()))
print(solve(fox, int(input())))

