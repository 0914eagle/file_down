
import math

def solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def angle(x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    def ball_collision(x1, y1, x2, y2, r):
        distance_between_centers = distance(x1, y1, x2, y2)
        return distance_between_centers <= 2*r

    def is_possible_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
        if not (0 <= x1 <= w and 0 <= x2 <= w and 0 <= x3 <= w and 0 <= y1 <= l and 0 <= y2 <= l and 0 <= y3 <= l):
            return False

        if not (r <= h and h <= 0.5*l):
            return False

        if not (ball_collision(x1, y1, x2, y2, 2*r) and ball_collision(x1, y1, x3, y3, 2*r)):
            return False

        return True

    if not is_possible_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
        return "impossible"

    d = distance(0, h, x1, y1)
    theta = angle(x1, y1, x2, y2)
    return f"{d:.2f} {theta:.2f}"

# Input parsing
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Call the function and print the result
print(solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h))
```
