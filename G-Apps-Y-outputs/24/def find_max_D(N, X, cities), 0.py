
def find_max_D(N, X, cities):
    max_D = 0
    for city in cities:
        distance = abs(city - X)
        if distance > max_D:
            max_D = distance
    return max_D

# Input processing
N, X = map(int, input().split())
cities = list(map(int, input().split()))

# Find and print the maximum value of D
max_D = find_max_D(N, X, cities)
print(max_D)
