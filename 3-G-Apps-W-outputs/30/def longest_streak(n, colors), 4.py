
def longest_streak(n, colors):
    color_count = {}
    streak_length = 0
    max_streak = 0

    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

        streak_length += 1

        if len(color_count) == 1 or len(color_count) == 2:
            max_streak = max(max_streak, streak_length)
        elif len(color_count) == 3:
            if min(color_count.values()) == 1:
                max_streak = max(max_streak, streak_length - 1)
            else:
                max_streak = max(max_streak, streak_length)

    return max_streak

# Input reading
n = int(input())
colors = list(map(int, input().split()))

# Output
print(longest_streak(n, colors))
