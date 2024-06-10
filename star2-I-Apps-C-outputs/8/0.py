
import math
def solve(opponents):
    def intersect(opponent):
        x, y, r = opponent
        d = math.sqrt(x*x + y*y)
        if d > r:
            return 0
        if d + r < 1:
            return 2
        theta = math.asin(r/d)
        return 2*theta/math.pi
    return max(map(intersect, opponents))

