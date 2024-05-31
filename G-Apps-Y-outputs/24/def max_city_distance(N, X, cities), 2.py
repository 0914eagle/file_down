
def max_city_distance(N, X, cities):
    max_d = 0
    for city in cities:
        d = abs(city - X)
        max_d = max(max_d, d)
    return max_d

# Input processing
N, X = map(int, input().split())
cities = list(map(int, input().split()))

# Calculate and print the maximum value of D
print(max_city_distance(N, X, cities))
