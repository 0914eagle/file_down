
def calculate_remaining_sand(X, t):
    remaining_sand = max(0, X - t)
    return remaining_sand

X, t = map(int, input().split())
result = calculate_remaining_sand(X, t)
print(result)
```