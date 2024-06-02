
def proportion_watered(a, b, c, d):
    a = a % 90
    b = b % 90
    c = c % 90
    d = d % 90

    angles = [a, b, c, d]
    angles.sort()

    if angles[0] == 0 and angles[3] == 90:
        return 1.0

    if angles[0] == 0:
        return (angles[3] - angles[1]) / 360.0

    if angles[3] == 90:
        return (angles[2] - angles[0]) / 360.0

    return (angles[2] - angles[0]) / 360.0

# Input
a, b, c, d = map(float, input().split())

# Output
print("{:.6f}".format(proportion_watered(a, b, c, d)))
