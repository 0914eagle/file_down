
def min_button_presses(n, m, brightness_levels):
    counts = [0] * m
    for i in range(1, n):
        diff = abs(brightness_levels[i] - brightness_levels[i-1])
        counts[diff % m] += 1
        if diff > 0:
            counts[m - (diff % m)] += 1

    min_presses = sum(min(counts[i], n - counts[i]) for i in range(m))
    return min_presses

n, m = map(int, input().split())
brightness_levels = list(map(int, input().split()))

result = min_button_presses(n, m, brightness_levels)
print(result)
```
