
def min_road_width(n, h, heights):
    road_width = 0
    for height in heights:
        if height > h:
            road_width += 2
        else:
            road_width += 1
    return road_width

# Input processing
n, h = map(int, input().split())
heights = list(map(int, input().split()))

# Output
print(min_road_width(n, h, heights))
