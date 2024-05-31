
def minimum_road_width(n, h, heights):
    width = 0
    for height in heights:
        if height > h:
            width += 2
        else:
            width += 1
    return width

# Input
n, h = map(int, input().split())
heights = list(map(int, input().split()))

# Output
print(minimum_road_width(n, h, heights))
