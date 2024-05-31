
def max_d_to_visit_cities(N, X, cities):
    max_distance = 0
    for city in cities:
        distance = abs(X - city)
        max_distance = max(max_distance, distance)
    
    return max_distance

# Input reading
N, X = map(int, input().split())
cities = list(map(int, input().split()))

# Calculate and output the maximum value of D
print(max_d_to_visit_cities(N, X, cities))
