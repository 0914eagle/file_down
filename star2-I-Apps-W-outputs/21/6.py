
def get_min_90_degree_turns(x):
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
    return get_min_90_degree_turns(x - 90) + 1

x = int(input())
print(get_min_90_degree_turns(x))
