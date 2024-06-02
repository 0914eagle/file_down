
def largest_streak(n, colors):
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

        if len(color_count) == 1 or len(color_count) == 2:
            max_streak = max(max_streak, streak)
        elif len(color_count) == 3:
            if min(color_count.values()) == 1:
                max_streak = max(max_streak, streak - 1)
            else:
                max_streak = max(max_streak, streak)

    return max_streak

# Input
n = int(input())
colors = list(map(int, input().split()))

# Output
print(largest_streak(n, colors))
