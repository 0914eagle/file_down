
def largest_streak(n, colors):
    color_count = {}
    streak_length = 0
    max_streak = 0

    for color in colors:
        color_count[color] = color_count.get(color, 0) + 1
        streak_length += 1

        if len(color_count) > 2:
            color_count.pop(colors[streak_length - len(color_count)])

        max_streak = max(max_streak, streak_length)

    return max_streak

# Input
n = int(input())
colors = list(map(int, input().split()))

# Output
print(largest_streak(n, colors))
