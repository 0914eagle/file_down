
import math

def check_collision(x1, y1, x2, y2, r):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    if dist <= 2 * r:
        return True
    return False

def solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h):
    d = x1 - r
    theta = math.atan2(y2 - y1, x2 - x1) * 180 / math.pi
    if check_collision(x1, y1, x2, y2, r):
        return "impossible"
    
    angle_B1C = math.atan2(y3 - y1, x3 - x1)
    angle_BC = math.atan2(y1 - y2, x1 - x2)
    angle_B1H = math.pi / 2 - angle_B1C
    angle_HB2 = math.pi - angle_B1H - angle_BC
    angle_HB2 *= 180 / math.pi
    
    y_pos = h + 2 * r
    x_pos = w - r

    if math.cos(angle_HB2) * dist < 2 * r:
        return "impossible"

    return f"{d:.2f} {theta:.2f}"

# Read input values
w, l = map(int, input().split())
r, x1, y1, x2, y2, x3, y3, h = map(int, input().split())

# Call the function and print the result
result = solve_trick_shot(w, l, r, x1, y1, x2, y2, x3, y3, h)
print(result)
```

