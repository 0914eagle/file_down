
def remaining_participants(n, k, m, cities):
    city_counts = {}
    total_remaining = 0
    
    for city in cities:
        if city not in city_counts:
            city_counts[city] = 0
        city_counts[city] += 1
    
    for city, count in city_counts.items():
        teams = count // k
        remaining = count - teams * k
        total_remaining += remaining * m
    
    return total_remaining

# Input parsing
n, k, m = map(int, input().split())
cities = list(map(int, input().split()))

# Call the function and output the result
print(remaining_participants(n, k, m, cities))
```
