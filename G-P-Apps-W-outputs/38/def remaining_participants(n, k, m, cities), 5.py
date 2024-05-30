
def remaining_participants(n, k, m, cities):
    city_count = {}
    for city in cities:
        if city in city_count:
            city_count[city] += 1
        else:
            city_count[city] = 1

    teams_formed = 0
    remaining = 0
    for city, count in city_count.items():
        teams = count // k
        teams_formed += teams
        remaining += count - (teams * k)

    remaining = remaining + (teams_formed * n * m) - (teams_formed * k)
    return max(0, n * m - remaining)

# Input parsing
n, k, m = map(int, input().split())
cities = list(map(int, input().split()))

print(remaining_participants(n, k, m, cities))
```
