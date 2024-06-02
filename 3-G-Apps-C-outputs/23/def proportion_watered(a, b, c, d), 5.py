
def proportion_watered(a, b, c, d):
    total_angle = 360
    angles = [a, b, c, d]
    angles.sort()
    
    if angles[0] == 0 and angles[3] == 90:
        return 1.0
    
    if angles[0] == 0:
        return (angles[3] / total_angle)
    
    if angles[3] == 90:
        return 1 - (angles[0] / total_angle)
    
    return (angles[3] - angles[0]) / total_angle

# Input
a, b, c, d = map(float, input().split())

# Output
print("{:.6f}".format(proportion_watered(a, b, c, d)))
