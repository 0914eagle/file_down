
import math

def minimum_distance(N, M, hotels, restaurants):
    min_distance = float('inf')
    restaurant_index = 0

    for i, (rx, ry) in enumerate(restaurants):
        max_distance = 0
        for hx, hy in hotels:
            distance = abs(rx - hx) + abs(ry - hy)
            max_distance = max(max_distance, distance)

        if max_distance < min_distance:
            min_distance = max_distance
            restaurant_index = i + 1

    return min_distance, restaurant_index

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

optimal_distance, restaurant_index = minimum_distance(N, M, hotels, restaurants)
print(optimal_distance)
print(restaurant_index)
```
