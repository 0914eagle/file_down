
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
        
        if len(color_counts) == 1 or len(color_counts) == 2:
            max_streak = max(max_streak, streak_length)
        elif len(color_counts) == 3:
            if min(color_counts.values()) == 1 and max(color_counts.values()) - 1 == sum(color_counts.values()) - max(color_counts.values()):
                max_streak = max(max_streak, streak_length)
        else:
            if min(color_counts.values()) == 1 and max(color_counts.values()) == 1:
                max_streak = max(max_streak, streak_length)
            else:
                color_counts[colors[i - streak_length + 1]] -= 1
                streak_length -= 1
    
    return max_streak

# Input reading
n = int(input())
colors = list(map(int, input().split()))

# Call the function and print the result
print(largest_streak(n, colors))
