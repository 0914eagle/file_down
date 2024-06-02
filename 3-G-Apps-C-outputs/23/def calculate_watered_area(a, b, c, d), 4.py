
def calculate_watered_area(a, b, c, d):
    total_angle = 360 - a - b - c - d
    if total_angle == 360:
        return 1.0
    elif total_angle == 0:
        return 0.0
    else:
        watered_area = total_angle / 360
        return watered_area

# Input
a, b, c, d = map(float, input().split())

# Output
print(calculate_watered_area(a, b, c, d))
