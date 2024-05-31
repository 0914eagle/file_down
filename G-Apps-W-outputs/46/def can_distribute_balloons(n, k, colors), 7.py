
def can_distribute_balloons(n, k, colors):
    color_count = {}
    
    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
    max_balloon_per_color = (n + k - 1) // k
    
    for count in color_count.values():
        if count > max_balloon_per_color:
            return "NO"
    
    return "YES"

# Input
n, k = map(int, input().split())
colors = input().strip()

# Output
print(can_distribute_balloons(n, k, colors))
