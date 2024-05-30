
import math

def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def find_optimal_restaurant(N, M, hotels, restaurants):
    min_distance = math.inf
    optimal_restaurant = -1

    for i, restaurant in enumerate(restaurants, 1):
        total_distance = 0
        for hotel in hotels:
            total_distance += min([calculate_distance(hotel[0], hotel[1], restaurant[0], restaurant[1]) for restaurant in restaurants])
        
        if total_distance < min_distance:
            min_distance = total_distance
            optimal_restaurant = i

    return min_distance, optimal_restaurant

# Input parsing
N, M = map(int, input().split())
C = int(input())
hotels = [tuple(map(int, input().split())) for _ in range(C)]
H = int(input())
restaurants = [tuple(map(int, input().split())) for _ in range(H)]

# Find optimal restaurant
optimal_distance, optimal_restaurant = find_optimal_restaurant(N, M, hotels, restaurants)

# Output results
print(optimal_distance)
print(optimal_restaurant)
```