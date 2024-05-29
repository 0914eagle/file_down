
def calculate_presses(n, m, brightness_levels):
    total_presses = 0
    for i in range(1, n):
        diff = abs(brightness_levels[i] - brightness_levels[i-1])
        total_presses += min(diff, m - diff)
    return total_presses

def min_presses(n, m, brightness_levels):
    min_presses_count = float('inf')
    favorite_brightness = None
    for x in range(1, m+1):
        current_presses = calculate_presses(n, m, [(a - 1 + x) % m + 1 for a in brightness_levels])
        if current_presses < min_presses_count:
            min_presses_count = current_presses
            favorite_brightness = x
    return min_presses_count

# Reading input
n, m = map(int, input().split())
brightness_levels = list(map(int, input().split()))

# Output minimum number of times Snuke needs to press the buttons
print(min_presses(n, m, brightness_levels))
```
