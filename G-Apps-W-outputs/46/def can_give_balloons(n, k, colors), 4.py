
def can_give_balloons(n, k, colors):
    color_count = {}
    for color in colors:
        if color not in color_count:
            color_count[color] = 0
        color_count[color] += 1
    
    max_same_color = max(color_count.values())
    
    if max_same_color <= k:
        return "YES"
    else:
        return "NO"

# Reading input
n, k = map(int, input().split())
colors = input().strip()

# Checking if Kefa can give out all balloons
result = can_give_balloons(n, k, colors)
print(result)
