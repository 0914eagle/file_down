
def can_distribute_balloons(n, k, colors):
    color_count = {}
    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    max_color_count = max(color_count.values())

    if max_color_count > k:
        return "NO"
    else:
        return "YES"

# Input
n, k = map(int, input().split())
colors = input().strip()

# Output
print(can_distribute_balloons(n, k, colors))
