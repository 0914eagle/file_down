
def can_distribute_balloons(n, k, colors):
    color_count = {}
    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    for color in color_count:
        if color_count[color] > k:
            return "NO"

    return "YES"

# Input processing
n, k = map(int, input().split())
colors = input().strip()

# Call the function and print the result
result = can_distribute_balloons(n, k, colors)
print(result)
