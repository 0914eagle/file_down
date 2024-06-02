
def proportion_watered(a, b, c, d):
    total_angle = 360
    angles = [a, b, c, d]
    angles.sort()
    
    if angles[0] == 0 and angles[1] == 0 and angles[2] == 0 and angles[3] == 0:
        return 1.0
    
    if angles[0] == 0 and angles[1] == 0 and angles[2] == 0:
        return 0.5
    
    if angles[0] == 0:
        return 0.25
    
    if angles[0] + angles[1] == 180:
        return 0.5
    
    if angles[0] + angles[1] + angles[2] == 270:
        return 0.75
    
    return 1.0

# Input
a, b, c, d = map(float, input().split())

# Output
print(proportion_watered(a, b, c, d))
