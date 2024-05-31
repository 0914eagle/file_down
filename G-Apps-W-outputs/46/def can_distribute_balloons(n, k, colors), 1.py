
def can_distribute_balloons(n, k, colors):
    color_counts = {}
    for color in colors:
        if color in color_counts:
            color_counts[color] += 1
        else:
            color_counts[color] = 1
    
    max_balloon_count = max(color_counts.values())
    
    if max_balloon_count <= (n + k - 1) // k:
        return "YES"
    else:
        return "NO"

# Input
n, k = map(int, input().split())
colors = input().strip()

# Output
print(can_distribute_balloons(n, k, colors))
