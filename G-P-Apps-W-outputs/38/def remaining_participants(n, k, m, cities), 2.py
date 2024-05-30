
def remaining_participants(n, k, m, cities):
    city_count = {}
    for city in cities:
        if city in city_count:
            city_count[city] += 1
        else:
            city_count[city] = 1
    
    min_count = min(city_count.values())
    total_teams = min_count * m
    remaining = total_teams * n
    
    return max(0, remaining - total_teams * k)

# Reading input
n, k, m = map(int, input().split())
cities = list(map(int, input().split()))

# Calling the function and printing the output
print(remaining_participants(n, k, m, cities))
```
