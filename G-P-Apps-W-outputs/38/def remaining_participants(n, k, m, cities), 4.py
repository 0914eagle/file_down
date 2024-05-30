
def remaining_participants(n, k, m, cities):
    city_counts = {}
    for city in cities:
        if city in city_counts:
            city_counts[city] += 1
        else:
            city_counts[city] = 1

    teams = 0
    remaining = 0
    for city, count in city_counts.items():
        teams += (count // k) * m
        remaining += count % k

    remaining += (teams // n) * n
    return n - remaining

# Input parsing
n, k, m = map(int, input().split())
cities = list(map(int, input().split()))

print(remaining_participants(n, k, m, cities))
```
