
def longest_streak(n, colors):
    color_count = {}
    streak_length = 0
    max_streak = 0
    
    for i in range(n):
        color = colors[i]
        color_count[color] = color_count.get(color, 0) + 1
        streak_length += 1
        
        max_count = max(color_count.values())
        other_count = streak_length - max_count
        
        if max_count - 1 == other_count:
            max_streak = max(max_streak, streak_length)
        elif max_count == 1 and len(color_count) == streak_length:
            max_streak = max(max_streak, streak_length - 1)
    
    return max_streak

# Input reading
n = int(input())
colors = list(map(int, input().split()))

# Call the function and print the result
print(longest_streak(n, colors))
