
def build_playing_schedule(n, m):
    teams = [chr(65 + i) for i in range(m)]
    players = [f"{team}{j}" for team in teams for j in range(1, n + 1)]

    schedule = []
    rounds = (m - 1) * n  # Total number of rounds
    games_per_round = n // 2  # Number of games in each round

    for round_num in range(rounds):
        round_schedule = []
        for game_num in range(games_per_round):
            player1 = players[(round_num + game_num) % len(players)]
            player2 = players[(round_num + 2 * game_num) % len(players)]
            round_schedule.append(f"{player1}-{player2}")
        schedule.append(" ".join(round_schedule))

    return schedule

n, m = map(int, input().split())
schedule = build_playing_schedule(n, m)

for round_schedule in schedule:
    print(round_schedule)
```
