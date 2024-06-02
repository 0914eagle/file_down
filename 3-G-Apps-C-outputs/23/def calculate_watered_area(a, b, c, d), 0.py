
import math

def calculate_watered_area(a, b, c, d):
    a = math.radians(a)
    b = math.radians(b)
    c = math.radians(c)
    d = math.radians(d)

    x1 = math.tan(a)
    x2 = math.tan(b)
    x3 = math.tan(c)
    x4 = math.tan(d)

    total_area = 1

    if a < math.pi/2:
        total_area -= 0.5 - 0.5 * x1
    if b < math.pi/2:
        total_area -= 0.5 - 0.5 * x2
    if c < math.pi/2:
        total_area -= 0.5 - 0.5 * x3
    if d < math.pi/2:
        total_area -= 0.5 - 0.5 * x4

    return round(total_area, 6)

# Input
a, b, c, d = map(float, input().split())

# Output
print(calculate_watered_area(a, b, c, d))
