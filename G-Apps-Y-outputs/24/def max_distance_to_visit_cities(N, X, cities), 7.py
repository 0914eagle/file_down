
def max_distance_to_visit_cities(N, X, cities):
    max_d = 0
    for city in cities:
        d = abs(city - X)
        if d > max_d:
            max_d = d
    return max_d

# Input
N, X = map(int, input().split())
cities = list(map(int, input().split()))

# Output
print(max_distance_to_visit_cities(N, X, cities))
