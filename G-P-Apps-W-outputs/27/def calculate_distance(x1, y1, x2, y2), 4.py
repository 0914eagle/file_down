
import math

def calculate_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def find_optimal_restaurant(N, M, hotels, restaurants):
    min_distance = math.inf
    optimal_restaurant = None

    for i, restaurant in enumerate(restaurants, start=1):
        total_distance = 0
        for hotel in hotels:
            hotel_x, hotel_y = hotel
            total_distance += min([calculate_distance(hotel_x, hotel_y, restaurant_x, restaurant_y) for restaurant_x, restaurant_y in restaurants])

        if total_distance < min_distance:
            min_distance = total_distance
            optimal_restaurant = i

    return min_distance, optimal_restaurant

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
