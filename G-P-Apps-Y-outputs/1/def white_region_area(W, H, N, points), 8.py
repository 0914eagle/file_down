
def white_region_area(W, H, N, points):
    white_area = W * H
    for x, y, a in points:
        if a == 1:
            white_area -= x * H
        elif a == 2:
            white_area -= (W - x) * H
        elif a == 3:
            white_area -= W * y
        else:
            white_area -= W * (H - y)
    
    return white_area

# Input processing
W, H, N = map(int, input().split())
points = [list(map(int, input().split())) for _ in range(N)]

# Calculate and output the white region area
print(white_region_area(W, H, N, points))
```
