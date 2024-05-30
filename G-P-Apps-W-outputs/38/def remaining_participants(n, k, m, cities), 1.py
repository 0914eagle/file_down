
def remaining_participants(n, k, m, cities):
    total_participants = n * m
    team_size = k * m
    teams_formed = total_participants // team_size

    remaining_participants = total_participants - teams_formed * team_size

    return remaining_participants

# Reading input
n, k, m = map(int, input().split())
cities = list(map(int, input().split()))

# Calling the function and printing the output
print(remaining_participants(n, k, m, cities))
```
