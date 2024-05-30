
def calculate_white_area(W, H, N, points):
    black_area = 0

    for x, y, a in points:
        if a == 1:
            black_area += x
        elif a == 2:
            black_area += W - x
        elif a == 3:
            black_area += y
        elif a == 4:
            black_area += H - y

    white_area = W * H - black_area
    return white_area

# Read input
W, H, N = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print output
result = calculate_white_area(W, H, N, points)
print(result)
```
