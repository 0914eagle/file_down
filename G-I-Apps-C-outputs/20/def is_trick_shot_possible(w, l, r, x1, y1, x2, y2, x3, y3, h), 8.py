
import math

def is_trick_shot_possible(w, l, r, x1, y1, x2, y2, x3, y3, h):
    # Check if the balls are in valid positions
    if y1 <= h + r or y2 <= h + r or y3 <= h + r:
        return False

    # Calculate the distances between the balls
    dist_12 = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    dist_13 = math.sqrt((x3 - x1)**2 + (y3 - y1)**2)
    
    # Calculate the angles of the shots
    angle_12 = math.degrees(math.atan2(y2 - y1, x2 - x1))
    angle_13 = math.degrees(math.atan2(y3 - y1, x3 - x1))
    
    # Check if the angles are correct for the trick shot
    if angle_12 < 0:
        angle_12 += 360
    if angle_13 < 0:
        angle_13 += 360
    if angle_12 > 90 or angle_13 > 90:
        return False

    return True, round(dist_12, 2), round(angle_12, 2)

# Read input values
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Check if trick shot is possible and calculate distance and angle
possible, dist, angle = is_trick_shot_possible(w, l, r, x1, y1, x2, y2, x3, y3, h)

if possible:
    print("{:.2f} {:.2f}".format(dist, angle))
else:
    print("impossible")
```
