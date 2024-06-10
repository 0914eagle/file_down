
def get_min_turns(x):
    x = x % 360
    if x < 0:
        x += 360
    
    if x == 0 or x == 180:
        return 0
    
    if x == 90 or x == 270:
        return 1
    
    if x == 30 or x == 150 or x == 210 or x == 330:
        return 3
    
    return 2

x = int(input())
print(get_min_turns(x))

