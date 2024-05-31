
def min_width_of_road(n, h, heights):
    total_width = 0
    for height in heights:
        if height > h:
            total_width += 2
        else:
            total_width += 1
    return total_width

# Input parsing
n, h = map(int, input().split())
heights = list(map(int, input().split()))

# Output the result
print(min_width_of_road(n, h, heights))
