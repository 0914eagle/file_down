
def calculate_min_presses(n, m, a):
    total_presses = 0
    current_brightness = a[0]

    for i in range(1, n):
        diff = a[i] - current_brightness

        if diff < 0:
            diff += m

        total_presses += min(diff, m - diff)
        current_brightness = a[i]

    return total_presses

n, m = map(int, input().split())
a = list(map(int, input().split()))

min_presses = min(calculate_min_presses(n, m, a), calculate_min_presses(n, m, a[::-1]))
print(min_presses)
```
