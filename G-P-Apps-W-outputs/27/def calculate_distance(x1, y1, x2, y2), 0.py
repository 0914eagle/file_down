
import math

def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def choose_optimal_restaurant(N, M, hotels, restaurants):
    max_dist = float('inf')
    optimal_restaurant = None

    for i, (rx, ry) in enumerate(restaurants, start=1):
        min_dist = max([calculate_distance(hx, hy, rx, ry) for hx, hy in hotels])
        if min_dist < max_dist:
            max_dist = min_dist
            optimal_restaurant = i

    return max_dist, optimal_restaurant

# Input parsing
N, M = map(int, input().split())
C = int(input())
hotels = [tuple(map(int, input().split())) for _ in range(C)]
H = int(input())
restaurants = [tuple(map(int, input().split())) for _ in range(H)]

# Choose optimal restaurant
optimal_distance, optimal_restaurant_index = choose_optimal_restaurant(N, M, hotels, restaurants)

# Output
print(optimal_distance)
print(optimal_restaurant_index)
```
