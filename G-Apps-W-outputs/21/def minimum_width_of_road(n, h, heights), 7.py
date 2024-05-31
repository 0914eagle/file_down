
def minimum_width_of_road(n, h, heights):
    min_width = 0
    for height in heights:
        if height > h:
            min_width += 2
        else:
            min_width += 1
    return min_width

# Input processing
n, h = map(int, input().split())
heights = list(map(int, input().split()))

# Call the function and print the result
result = minimum_width_of_road(n, h, heights)
print(result)
