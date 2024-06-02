
def calculate_watered_area(a, b, c, d):
    total_angle = 360 - a - b - c - d
    if total_angle == 360:
        return 1.0
    elif total_angle == 0:
        return 0.0
    else:
        return 1 - (abs((180 - a) % 180 - 90) + abs((180 - b) % 180 - 90) + abs((180 - c) % 180 - 90) + abs((180 - d) % 180 - 90)) / 360

# Input
a, b, c, d = map(float, input().split())

# Output
print("{:.6f}".format(calculate_watered_area(a, b, c, d)))
