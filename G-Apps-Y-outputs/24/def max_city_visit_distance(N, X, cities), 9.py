
def max_city_visit_distance(N, X, cities):
    max_dist = 0
    for city in cities:
        dist = abs(X - city)
        if dist > max_dist:
            max_dist = dist
    return max_dist

# Input processing
input_data = input().strip().split()
N = int(input_data[0])
X = int(input_data[1])
cities = list(map(int, input().strip().split()))

# Output the maximum value of D
print(max_city_visit_distance(N, X, cities))
