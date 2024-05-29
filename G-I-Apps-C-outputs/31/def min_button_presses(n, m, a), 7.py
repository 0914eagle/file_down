
def min_button_presses(n, m, a):
    total_presses = 0
    current_brightness = a[0]
    
    for i in range(1, n):
        diff = abs(a[i] - current_brightness)
        total_presses += min(diff, m - diff)
        current_brightness = a[i]

    return total_presses

# Reading input
n, m = map(int, input().split())
a = list(map(int, input().split()))

# Finding the minimum number of button presses needed
result = min_button_presses(n, m, a)
print(result)
```
