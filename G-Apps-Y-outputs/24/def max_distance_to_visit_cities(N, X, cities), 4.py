
def max_distance_to_visit_cities(N, X, cities):
    max_distance = 0
    
    for city in cities:
        distance = abs(city - X)
        max_distance = max(max_distance, distance)
    
    return max_distance

# Input
N, X = map(int, input().split())
cities = list(map(int, input().split()))

# Output
print(max_distance_to_visit_cities(N, X, cities))
