
import math

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_optimal_distance(N, M, hotels, restaurants):
    min_distance = math.inf
    optimal_restaurant = -1

    for i, restaurant in enumerate(restaurants, start=1):
        max_distance = 0
        for hotel in hotels:
            max_distance = max(max_distance, distance(hotel[0], hotel[1], restaurant[0], restaurant[1]))
        if max_distance < min_distance:
            min_distance = max_distance
            optimal_restaurant = i

    return min_distance, optimal_restaurant

# Input parsing
N, M = map(int, input().split())
C = int(input())
hotels = [tuple(map(int, input().split())) for _ in range(C)]
H = int(input())
restaurants = [tuple(map(int, input().split())) for _ in range(H)]

# Find optimal distance and restaurant
optimal_distance, optimal_restaurant = find_optimal_distance(N, M, hotels, restaurants)

# Output
print(optimal_distance)
print(optimal_restaurant)
```

