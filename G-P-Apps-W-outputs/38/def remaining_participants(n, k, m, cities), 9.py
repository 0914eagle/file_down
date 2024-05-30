
def remaining_participants(n, k, m, cities):
    city_counts = {}
    
    for city in cities:
        if city in city_counts:
            city_counts[city] += 1
        else:
            city_counts[city] = 1
    
    remaining = n * m
    team_count = 0
    
    for city, count in city_counts.items():
        team_count += count // k
        remaining -= count // k * k
    
    return remaining

# Input processing
n, k, m = map(int, input().split())
cities = list(map(int, input().split()))

# Output
print(remaining_participants(n, k, m, cities))
```
