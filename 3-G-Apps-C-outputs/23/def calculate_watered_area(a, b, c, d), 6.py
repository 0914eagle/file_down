
def calculate_watered_area(a, b, c, d):
    total_angle = 360 - a - b - c - d
    if total_angle == 360:
        return 1.0
    elif total_angle == 0:
        return 0.0
    else:
        return 1 - (a + b) / 360 - (b + c) / 360 - (c + d) / 360 - (d + a) / 360

# Input
a, b, c, d = map(float, input().split())

# Calculate and output the proportion of the area watered by the sprinklers
print(calculate_watered_area(a, b, c, d))
