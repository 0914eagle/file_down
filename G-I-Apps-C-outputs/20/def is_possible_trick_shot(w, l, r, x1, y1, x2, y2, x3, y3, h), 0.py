
import math

def is_possible_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def angle(x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    def find_intersection_point(x1, y1, x2, y2, x3, y3, r):
        d = distance(x1, y1, x3, y3) - 2*r
        theta = angle(x1, y1, x3, y3)
        x = x3 + d * math.cos(math.radians(theta))
        y = y3 + d * math.sin(math.radians(theta))
        return x, y
    
    # Calculating intersection points for each possible shot
    intersection_1_2 = find_intersection_point(x1, y1, x2, y2, x3, y3, r)
    intersection_2_3 = find_intersection_point(x2, y2, x3, y3, x1, y1, r)

    d, theta = intersection_1_2
    # Check if intersection points are within the table boundaries and if the cue ball is on the dashed line
    if 0 <= d <= w and 0 <= intersection_2_3[0] <= w and 0 <= x1 <= w and h <= y1 <= l - r:
        return format(d, '.2f'), format(theta, '.2f')
    else:
        return "impossible"

# Input reading
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Check if trick shot is possible
result = is_possible_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h)

# Output
print(result)
```
