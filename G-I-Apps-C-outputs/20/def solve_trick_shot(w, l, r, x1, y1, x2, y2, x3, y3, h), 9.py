
import math

def solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def get_angle(x1, y1, x2, y2):
        angle_rad = math.atan2(y2 - y1, x2 - x1)
        angle_deg = math.degrees(angle_rad)
        return angle_deg if angle_deg >= 0 else angle_deg + 360

    # Calculate distances from each ball to the pockets
    dist_1_to_pocket = distance(x1, y1, 0, l)
    dist_2_to_pocket = distance(x2, y2, 0, l)
    dist_3_to_pocket = distance(x3, y3, w, l)

    # Check if the trick shot is possible
    if dist_1_to_pocket <= r + 2 * r and dist_2_to_pocket <= r + 2 * r and dist_3_to_pocket <= r + 2 * r:
        # Calculate the angle needed to shoot the cue ball
        angle_1_to_2 = get_angle(x1, y1, x2, y2)
        angle_2_to_3 = get_angle(x2, y2, x3, y3)

        return round(math.sqrt((x1 - x2)**2 + (y1 - y2)**2), 2), round(angle_1_to_2, 2)
    else:
        return "impossible"

# Input parsing
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Solve and output the trick shot
result = solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h)
if result == "impossible":
    print("impossible")
else:
    print(*result)
```
