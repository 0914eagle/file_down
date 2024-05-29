
def construct_playing_schedule(n, m):
    num_players = n * m
    total_rounds = n * (m - 1) + 1
    schedule = []

    teams = [chr(ord('A') + i) for i in range(m)]

    for r in range(total_rounds):
        round_schedule = []
        for i in range(m):
            team1 = teams[i]
            for j in range(n):
                player_idx = (r + i + j) % m
                team2 = teams[player_idx]
                player1 = team1 + str(j + 1)
                player2 = team2 + str((r + i + j) % n + 1)
                game = player1 + "-" + player2
                round_schedule.append(game)
        schedule.append(round_schedule)

    return schedule

# Input parsing
n, m = map(int, input().split())

# Construct playing schedule
playing_schedule = construct_playing_schedule(n, m)

# Output playing schedule
for round_schedule in playing_schedule:
    print(" ".join(round_schedule))
```
