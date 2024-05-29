
def min_button_presses(n, m, a):
    total_presses = 0
    for i in range(n-1):
        diff = abs(a[i] - a[i+1])
        total_presses += min(diff, m - diff)
    return total_presses

def find_favorite_brightness(n, m, a):
    candidate_brightness = set()
    for i in range(n-1):
        d = abs(a[i] - a[i+1])
        candidate_brightness.add(d)
        candidate_brightness.add(m - d)
    min_presses = float('inf')
    favorite_brightness = None
    for brightness in candidate_brightness:
        presses = min_button_presses(n, m, [a[0], brightness] + a[2:])
        if presses < min_presses:
            min_presses = presses
            favorite_brightness = brightness
    return min_presses

# Reading input
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Finding the favorite brightness level
result = find_favorite_brightness(n, m, a)
print(result)
```
