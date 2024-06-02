
def longest_streak(n, colors):
    color_count = {}
    streak = 0
    max_streak = 0

    for i in range(n):
        color = colors[i]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

        streak += 1

        if len(color_count) > 2:
            streak -= 1
            color_count[colors[i - streak]] -= 1
            if color_count[colors[i - streak]] == 0:
                del color_count[colors[i - streak]]

        max_streak = max(max_streak, streak)

    return max_streak

# Input reading
n = int(input())
colors = list(map(int, input().split()))

# Call the function and print the result
print(longest_streak(n, colors))
