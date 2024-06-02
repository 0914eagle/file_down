
def longest_streak(n, colors):
    color_count = {}
    streak_length = 0
    max_streak = 0

    for color in colors:
        color_count[color] = color_count.get(color, 0) + 1
        streak_length += 1

        if len(color_count) == 1 or len(color_count) == 2:
            max_streak = max(max_streak, streak_length)
        elif len(color_count) == 3:
            if min(color_count.values()) == 1 and max(color_count.values()) - min(color_count.values()) == 1:
                max_streak = max(max_streak, streak_length - 1)

    return max_streak

# Input reading
n = int(input())
colors = list(map(int, input().split()))

# Call the function and print the result
print(longest_streak(n, colors))
