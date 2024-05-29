
def construct_playing_schedule(n, m):
    teams = [chr(ord('A')+i) for i in range(m)]
    players = [f'{team}{j}' for team in teams for j in range(1, n+1)]
    
    games_per_round = (m-1) * n
    
    schedule = []
    
    for i in range(games_per_round):
        round_schedule = []
        for j in range(m):
            for k in range(n):
                opponent_team = (j + i % (m-1) + 1) % m
                opponent_player = f'{teams[opponent_team]}{k+1}'
                round_schedule.append(f'{players[j*n+k]}-{opponent_player}')
        schedule.append(' '.join(round_schedule))
    
    return schedule

n, m = map(int, input().split())
schedule = construct_playing_schedule(n, m)

for round_schedule in schedule:
    print(round_schedule)
```
