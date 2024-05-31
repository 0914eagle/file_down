
def min_stool_height(N, heights):
    max_height = 0
    total_height = 0

    for h in heights:
        if h >= max_height:
            max_height = h
        else:
            total_height += max_height - h

    return total_height

# Read input
N = int(input())
heights = list(map(int, input().split()))

# Call the function and print the result
print(min_stool_height(N, heights))
