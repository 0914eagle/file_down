
def average_rounded_up(a, b):
    x = (a + b) / 2
    return int(x + 0.5)

a, b = map(int, input().split())
result = average_rounded_up(a, b)
print(result)
```
