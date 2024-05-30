
def calculate_white_area(W, H, N, points):
    white_area = W * H
    for x, y, a in points:
        if a == 1:
            white_area -= x * H
        elif a == 2:
            white_area -= (W - x) * H
        elif a == 3:
            white_area -= W * y
        elif a == 4:
            white_area -= W * (H - y)
    return white_area

# Read input
W, H, N = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the white area
print(calculate_white_area(W, H, N, points))
```
