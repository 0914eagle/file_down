
def min_button_presses(n, m, brightness_levels):
    def press_forward(curr, target):
        forward_presses = 0
        while curr != target:
            curr = curr % m + 1
            forward_presses += 1
        return forward_presses

    def press_favorite(curr, target):
        return min(
            abs(curr - target),
            m - abs(curr - target)
        )

    total_presses = 0
    for i in range(n - 1):
        total_presses += min(
            press_forward(brightness_levels[i], brightness_levels[i + 1]),
            press_favorite(brightness_levels[i], brightness_levels[i + 1])
        )

    return total_presses

# Reading input
n, m = map(int, input().split())
brightness_levels = list(map(int, input().split()))

# Calling the function with input data
result = min_button_presses(n, m, brightness_levels)
print(result)
```
