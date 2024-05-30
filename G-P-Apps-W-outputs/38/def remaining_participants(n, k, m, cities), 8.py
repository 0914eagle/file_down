
def remaining_participants(n, k, m, cities):
    city_counts = {}
    for city in cities:
        if city in city_counts:
            city_counts[city] += 1
        else:
            city_counts[city] = 1
    
    total_teams = 0
    remaining_participants = 0
    for city, count in city_counts.items():
        teams_from_city = count // k
        total_teams += teams_from_city
        remaining_participants += count % k
    
    remaining_participants += total_teams * n * m
    
    return remaining_participants

# Input parsing
n, k, m = map(int, input().split())
cities = list(map(int, input().split()))

result = remaining_participants(n, k, m, cities)
print(result)
```
