
def can_distribute_balloons(n, k, colors):
    color_counts = {}
    for color in colors:
        if color not in color_counts:
            color_counts[color] = 1
        else:
            color_counts[color] += 1
    
    max_same_color_balloons = max(color_counts.values())
    
    if max_same_color_balloons > k:
        return "NO"
    else:
        return "YES"

# Reading input
n, k = map(int, input().split())
colors = input().strip()

# Calling the function and printing the result
print(can_distribute_balloons(n, k, colors))
