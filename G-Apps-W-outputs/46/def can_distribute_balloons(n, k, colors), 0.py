
def can_distribute_balloons(n, k, colors):
    color_count = {}
    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    for color, count in color_count.items():
        if count > k:
            return "NO"
    
    return "YES"

# Input
n, k = map(int, input().split())
colors = input().strip()

# Output
print(can_distribute_balloons(n, k, colors))
