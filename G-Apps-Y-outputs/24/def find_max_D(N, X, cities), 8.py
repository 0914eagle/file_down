
def find_max_D(N, X, cities):
    max_distance = 0
    for city in cities:
        distance = abs(X - city)
        if distance > max_distance:
            max_distance = distance
    return max_distance

# Input processing
N, X = map(int, input().split())
cities = list(map(int, input().split()))

# Find and print the maximum value of D
print(find_max_D(N, X, cities))
