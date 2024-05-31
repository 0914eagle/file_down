
def can_distribute_balloons(n, k, s):
    color_count = {}
    
    for color in s:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    
    max_same_color = max(color_count.values())
    
    if max_same_color > k:
        return "NO"
    else:
        return "YES"

# Input
n, k = map(int, input().split())
s = input().strip()

# Output
print(can_distribute_balloons(n, k, s))
