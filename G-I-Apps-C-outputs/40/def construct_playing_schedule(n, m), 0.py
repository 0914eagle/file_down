
def construct_playing_schedule(n, m):
    teams = [chr(ord('A') + i) for i in range(m)]
    players = [f"{team}{j}" for team in teams for j in range(1, n + 1)]

    total_rounds = (m - 1) * n + 1
    games_per_round = (m - 1) * n

    schedule = []
    for round_num in range(total_rounds):
        games = []
        for i in range(m):
            for j in range(n):
                opponent_team = (i + round_num) % m
                opponent_player = f"{teams[opponent_team]}{j + 1}"
                games.append(f"{players[i * n + j]}-{opponent_player}")
        schedule.append(" ".join(games))

    return schedule

# Input
n, m = map(int, input().split())

# Output
schedule = construct_playing_schedule(n, m)
for round_games in schedule:
    print(round_games)
