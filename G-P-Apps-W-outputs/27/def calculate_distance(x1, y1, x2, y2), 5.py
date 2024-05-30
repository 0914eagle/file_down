
import math

def calculate_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

def optimal_restaurant(N, M, hotels, restaurants):
    max_distance = float('inf')
    optimal_index = -1

    for i, restaurant in enumerate(restaurants):
        max_dist = 0
        for hotel in hotels:
            dist = calculate_distance(hotel[0], hotel[1], restaurant[0], restaurant[1])
            max_dist = max(max_dist, dist)
        
        if max_dist < max_distance:
            max_distance = max_dist
            optimal_index = i+1

    return max_distance, optimal_index

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

distance, index = optimal_restaurant(N, M, hotels, restaurants)
print(distance)
print(index)
```
