
import math
def distance(p1, p2):
return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
def hide_the_chickens():
roost = list(map(float, input().split()))
N = int(input())
hiding_spots = [list(map(float, input().split())) for _ in range(N)]
hiding_spots.sort(key=lambda spot: distance(spot, roost))
fox_position = roost
distance_traveled = 0
hen_count = 0
for hiding_spot in hiding_spots:
if hen_count == 2:
fox_position = hiding_spot
hen_count = 1
else:
distance_traveled += distance(fox_position, hiding_spot)
fox_position = hiding_spot
hen_count += 1
return distance_traveled
print(hide_the_chickens())

