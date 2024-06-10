
def get_min_rotations(x):
    x = x % 360
    if x == 0:
        return 0
    elif x == 90:
        return 1
    elif x == 180:
        return 2
    elif x == 270:
        return 3
    elif x < 90:
        return 1
    elif x < 180:
        return 2
    elif x < 270:
        return 3
    else:
        return 0

x = int(input())
print(get_min_rotations(x))

