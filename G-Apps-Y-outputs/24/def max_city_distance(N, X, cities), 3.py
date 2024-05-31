
def max_city_distance(N, X, cities):
    max_distance = 0
    for city in cities:
        distance = abs(X - city)
        max_distance = max(max_distance, distance)
    return max_distance

# Input processing
N, X = map(int, input().split())
cities = list(map(int, input().split()))

# Calculate and print the maximum value of D
print(max_city_distance(N, X, cities))
