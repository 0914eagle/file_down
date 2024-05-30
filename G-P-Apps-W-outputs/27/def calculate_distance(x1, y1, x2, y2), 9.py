
import math

def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_optimal_restaurant(N, M, hotels, restaurants):
    min_distance = float('inf')
    optimal_index = -1

    for i, (rx, ry) in enumerate(restaurants, start=1):
        max_distance = 0
        for hx, hy in hotels:
            distance = calculate_distance(hx, hy, rx, ry)
            max_distance = max(max_distance, distance)
        if max_distance < min_distance:
            min_distance = max_distance
            optimal_index = i

    return min_distance, optimal_index

# Input
N, M = map(int, input().split())
C = int(input())
hotels = [tuple(map(int, input().split())) for _ in range(C)]
H = int(input())
restaurants = [tuple(map(int, input().split())) for _ in range(H)]

# Output
distance, index = find_optimal_restaurant(N, M, hotels, restaurants)
print(distance)
print(index)
```
