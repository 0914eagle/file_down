
import math

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_optimal_restaurant(N, M, hotels, restaurants):
    min_distance = float('inf')
    optimal_restaurant = -1

    for i, (rx, ry) in enumerate(restaurants, start=1):
        max_distance = 0
        for hx, hy in hotels:
            max_distance = max(max_distance, distance(rx, ry, hx, hy))

        if max_distance < min_distance:
            min_distance = max_distance
            optimal_restaurant = i

    return min_distance, optimal_restaurant

# Input parsing
N, M = map(int, input().split())
hotels = []
restaurants = []

C = int(input())
for _ in range(C):
    x, y = map(int, input().split())
    hotels.append((x, y))

H = int(input())
for _ in range(H):
    x, y = map(int, input().split())
    restaurants.append((x, y))

# Find optimal restaurant
optimal_distance, optimal_restaurant = find_optimal_restaurant(N, M, hotels, restaurants)

# Output
print(optimal_distance)
print(optimal_restaurant)
```
