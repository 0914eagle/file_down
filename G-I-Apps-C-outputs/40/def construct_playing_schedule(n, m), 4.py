
def construct_playing_schedule(n, m):
    teams = [chr(ord('A') + i) for i in range(m)]

    playing_schedule = []
    total_rounds = (m - 1) * n + 1

    for round_num in range(total_rounds):
        games = []
        for team in teams:
            for i in range(1, n + 1):
                other_teams = [t for t in teams if t != team]
                for other_team in other_teams:
                    games.append(f"{team}{i}-{other_team}{(i + round_num) % n + 1}")
        playing_schedule.append(' '.join(games))

    return playing_schedule

# Input
n, m = map(int, input().split())

# Output
schedule = construct_playing_schedule(n, m)
for round_num, games in enumerate(schedule):
    print(f"Round {round_num + 1}: {games}")
```
