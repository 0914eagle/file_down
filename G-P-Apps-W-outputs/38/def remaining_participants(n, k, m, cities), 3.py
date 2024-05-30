
def remaining_participants(n, k, m, cities):
    city_counts = {}
    for city in cities:
        if city in city_counts:
            city_counts[city] += 1
        else:
            city_counts[city] = 1
    
    min_team_size = (m // n) * k
    remaining = 0

    for count in city_counts.values():
        remaining += max(0, count - min_team_size)

    return remaining

# Input processing
n, k, m = map(int, input().split())
cities = list(map(int, input().split()))

# Call the function with input values
result = remaining_participants(n, k, m, cities)
print(result)
```
