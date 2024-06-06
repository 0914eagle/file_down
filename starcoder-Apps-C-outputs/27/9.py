
import sys

def distance(x1,x2,y1,y2):
    return abs(x1-x2)+abs(y1-y2)

def closest_intersection(n,d,homes):
    total_distance = 0
    for home in homes:
        x,y = home[0],home[1]
        x_min = max(0,x-d)
        y_min = max(0,y-d)
        x_max = min(10**9,x+d)
        y_max = min(10**9,y+d)
        if (x,y) == (0,0):
            min_distance = 0
        elif x == 0:
            min_distance = y_max
        elif y == 0:
            min_distance = x_max
        elif x == y:
            min_distance = 2*x_max
        else:
            min_distance = min(x_max,y_max)
        total_distance += min_distance
    return total_distance

n = int(sys.stdin.readline())
d = int(sys.stdin.readline())
homes = [tuple(map(int,sys.stdin.readline().split())) for _ in range(n)]
print(closest_intersection(n,d,homes))
