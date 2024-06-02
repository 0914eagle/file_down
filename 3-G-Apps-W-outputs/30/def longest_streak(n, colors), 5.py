
def longest_streak(n, colors):
    color_count = {}
    streak_length = 0
    max_streak = 0

    for i in range(n):
        color = colors[i]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        streak_length += 1

        if len(color_count) == 2:
            if abs(list(color_count.values())[0] - list(color_count.values())[1]) == 1:
                max_streak = max(max_streak, streak_length)
        elif len(color_count) > 2:
            max_streak = max(max_streak, streak_length - 1)
            min_count = min(color_count.values())
            for key in color_count:
                if color_count[key] == min_count:
                    del color_count[key]
                    break
            streak_length -= 1

    return max_streak

# Input reading
n = int(input())
colors = list(map(int, input().split()))

# Output
print(longest_streak(n, colors))
