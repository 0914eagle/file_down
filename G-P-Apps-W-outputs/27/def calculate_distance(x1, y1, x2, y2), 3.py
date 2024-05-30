
import math

def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def choose_optimal_restaurant(N, M, hotels, restaurants):
    min_distance = math.inf
    optimal_restaurant = 0

    for i, restaurant in enumerate(restaurants, start=1):
        max_distance = 0
        for hotel in hotels:
            distance = calculate_distance(hotel[0], hotel[1], restaurant[0], restaurant[1])
            max_distance = max(max_distance, distance)
        
        if max_distance < min_distance:
            min_distance = max_distance
            optimal_restaurant = i

    return min_distance, optimal_restaurant

# Input parsing
N, M = map(int, input().split())
C = int(input())
hotels = [list(map(int, input().split())) for _ in range(C)]
H = int(input())
restaurants = [list(map(int, input().split())) for _ in range(H)]

# Find optimal restaurant
optimal_distance, optimal_restaurant = choose_optimal_restaurant(N, M, hotels, restaurants)

# Output
print(optimal_distance)
print(optimal_restaurant)
```
