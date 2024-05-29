
def construct_schedule(n, m):
    total_rounds = (m-1) * n + 1
    teams = [chr(ord('A') + i) for i in range(m)]

    schedule = []
    for round_num in range(total_rounds):
        games = []
        for i in range(m):
            team1 = teams[i]
            for j in range(n):
                team2_idx = (i + round_num + j) % m
                team2 = teams[team2_idx]

                player1 = team1 + str(j + 1)
                player2 = team2 + str((j + round_num) % n + 1)

                games.append(player1 + '-' + player2)

        schedule.append(' '.join(games))

    return schedule

# Input reading
n, m = map(int, input().split())

# Construct and print the schedule
for game_round in construct_schedule(n, m):
    print(game_round)
```
