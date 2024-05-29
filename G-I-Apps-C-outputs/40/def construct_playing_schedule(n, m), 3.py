
def construct_playing_schedule(n, m):
    teams = []
    for i in range(m):
        team = []
        for j in range(1, n + 1):
            team.append(chr(65 + i) + str(j))
        teams.append(team)

    rounds = []
    for r in range((m-1) * n):
        current_round = []
        for i in range(m):
            for j in range(n):
                game = teams[i][j] + '-' + teams[(i+r+1) % m][j]
                current_round.append(game)
        rounds.append(current_round)

    return rounds

n, m = map(int, input().split())
playing_schedule = construct_playing_schedule(n, m)
for round in playing_schedule:
    print(' '.join(round))
```
