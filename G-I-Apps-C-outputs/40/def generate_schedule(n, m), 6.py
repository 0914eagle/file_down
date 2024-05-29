
def generate_schedule(n, m):
    teams = [chr(ord('A') + i) for i in range(m)]
    players = [team + str(j) for team in teams for j in range(1, n + 1)]
    
    schedule = []
    total_rounds = (m - 1) * n + 1
    
    for rnd in range(total_rounds):
        round_games = []
        for i in range(n):
            for j in range(m):
                opponent_team = (j + rnd) % m
                for k in range(n):
                    opponent_player = teams[opponent_team] + str((i + k) % n + 1)
                    game = players[j*n+i] + '-' + opponent_player
                    round_games.append(game)
        schedule.append(' '.join(round_games))
    
    return schedule


# Input reading
n, m = map(int, input().split())

# Generate and print the schedule
schedule = generate_schedule(n, m)
for round in schedule:
    print(round)
``` 
