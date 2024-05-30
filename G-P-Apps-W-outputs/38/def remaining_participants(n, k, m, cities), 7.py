
def remaining_participants(n, k, m, cities):
    city_count = {}
    team_count = 0
    
    for city in cities:
        if city not in city_count:
            city_count[city] = 1
        else:
            city_count[city] += 1
        team_count += city_count[city] // k
        city_count[city] %= k
    
    remaining = n * m - team_count * k
    return max(0, remaining)

# Reading input
n, k, m = map(int, input().split())
cities = list(map(int, input().split()))

# Calling the function with input values
result = remaining_participants(n, k, m, cities)
print(result)
```
