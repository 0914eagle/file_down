
def remaining_participants(n, k, m, a):
    city_counts = {}
    for city in a:
        if city in city_counts:
            city_counts[city] += 1
        else:
            city_counts[city] = 1
    
    team_participants = (m // k) * n
    remaining_participants = m * n - team_participants
    
    for city in city_counts:
        teams_from_city = city_counts[city] // k
        remaining_participants -= teams_from_city * k
    
    return remaining_participants

# Reading input
n, k, m = map(int, input().split())
a = list(map(int, input().split()))

# Output
print(remaining_participants(n, k, m, a))
```
