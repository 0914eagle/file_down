
def average_rounded_up(a, b):
    x = (a + b) / 2
    if x % 1 == 0.5:  # Check if x is at a half point
        return int(x) + 1
    else:
        return round(x)

a, b = map(int, input().split())
print(average_rounded_up(a, b))
```
