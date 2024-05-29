
import math

def solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    def distance(x1, y1, x2, y2):
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def angle(x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))

    d = round((x1 - r), 2)
    theta12 = angle(x1, y1, x2, y2)
    theta13 = angle(x1, y1, x3, y3)
    dist12 = distance(x1, y1, x2, y2)
    dist13 = distance(x1, y1, x3, y3)

    if dist12 <= 2*r and dist13 <= 2*r and y1 <= h:
        print("{:.2f} {:.2f}".format(d, theta12))
    else:
        print("impossible")

# Sample Input
w, l = 20, 30
r, x1, y1, x2, y2, x3, y3, h = 2, 10, 20, 2, 24, 18, 28, 10
solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h)
