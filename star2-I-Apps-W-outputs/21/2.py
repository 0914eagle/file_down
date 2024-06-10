
def min_90_rotations(x):
    x = x % 360
    if x < 0:
        x += 360
    
    if x == 0:
        return 0
    
    if x == 90:
        return 1
    
    if x == 180:
        return 2
    
    if x == 270:
        return 3
    
    return min_90_rotations(x - 90) + 1
    
x = int(input())
print(min_90_rotations(x))

