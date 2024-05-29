
import math

def is_possible(w, l, r, x1, y1, x2, y2, x3, y3, h):
    def dist(x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def angle_diff(x1, y1, x2, y2):
        return math.degrees(math.atan2(y2 - y1, x2 - x1))
    
    def collide(x1, y1, x2, y2, r):
        return dist(x1, y1, x2, y2) <= 2*r
    
    def find_point(dx, dy, d):
        new_x = dx * d
        new_y = dy * d + h
        return new_x, new_y
    
    # Check if cue ball can hit ball 1
    if not collide(0, l-h, x1, y1, 2*r):
        return "impossible"
    
    # Calculate new direction for ball 1 after hit
    dx1 = (x1 - 0) / dist(x1, y1, 0, l-h)
    dy1 = (l-h - y1) / dist(x1, y1, 0, l-h)
    
    # Check if ball 1 can hit ball 2
    new_x2, new_y2 = find_point(dx1, dy1, 2*r)
    if not collide(x1, y1, new_x2, new_y2, r):
        return "impossible"
    
    # Calculate new direction for ball 2 after hit
    dx2 = (x2 - x1) / dist(x2, y2, x1, y1)
    dy2 = (y1 - y2) / dist(x2, y2, x1, y1)
    
    # Check if ball 2 can hit ball 3
    new_x3, new_y3 = find_point(dx2, dy2, 2*r)
    if not collide(x2, y2, new_x3, new_y3, r):
        return "impossible"
    
    # Calculate the required distance and angle for the cue ball
    d = dist(0, l-h, x1, y1) - 2*r
    theta = angle_diff(x1, y1, 0, l-h)
    
    return round(d, 2), round(theta, 2)

# Input
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Output
result = is_possible(w, l, r, x1, y1, x2, y2, x3, y3, h)
if isinstance(result, tuple):
    print(*result)
else:
    print(result)
```
