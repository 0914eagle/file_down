
def find_max_D(N, X, cities):
    max_D = 0
    for city in cities:
        distance = abs(city - X)
        max_D = max(max_D, distance)
    
    return max_D

# Input
N, X = map(int, input().split())
cities = list(map(int, input().split()))

# Output
print(find_max_D(N, X, cities))
