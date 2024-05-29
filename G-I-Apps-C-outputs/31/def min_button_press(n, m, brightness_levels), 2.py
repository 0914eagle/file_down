
def min_button_press(n, m, brightness_levels):
    def adjust_brightness(curr, target, m):
        dist1 = abs(target - curr)
        dist2 = m - dist1
        return min(dist1, dist2)

    min_presses = float("inf")
    for x in range(1, m+1):
        presses = 0
        for i in range(n-1):
            presses += adjust_brightness(brightness_levels[i], brightness_levels[i+1], m)
        min_presses = min(min_presses, presses)
    
    return min_presses

# Input processing
n, m = map(int, input().split())
brightness_levels = list(map(int, input().split()))

# Output
print(min_button_press(n, m, brightness_levels))
```
