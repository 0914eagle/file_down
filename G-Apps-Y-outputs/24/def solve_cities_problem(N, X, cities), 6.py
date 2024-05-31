
def solve_cities_problem(N, X, cities):
    distances = [abs(X - city) for city in cities]
    max_distance = max(distances)
    
    gcd = distances[0]
    for i in range(1, N):
        import math
        gcd = math.gcd(gcd, distances[i])
    
    return gcd

# Read input
N, X = map(int, input().split())
cities = list(map(int, input().split()))

# Call the function and print the result
result = solve_cities_problem(N, X, cities)
print(result)
