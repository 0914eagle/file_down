
def largest_streak(n, colors):
    color_counts = {}
    streak_length = 0
    max_streak = 0

    for i in range(n):
        color = colors[i]
        if color not in color_counts:
            color_counts[color] = 1
        else:
            color_counts[color] += 1

        streak_length += 1

        if len(color_counts) > 2:
            streak_length -= 1
            color_counts[colors[i - streak_length]] -= 1
            if color_counts[colors[i - streak_length]] == 0:
                del color_counts[colors[i - streak_length]]

        max_streak = max(max_streak, streak_length)

    return max_streak

# Input processing
n = int(input())
colors = list(map(int, input().split()))

# Call the function and print the result
print(largest_streak(n, colors))
