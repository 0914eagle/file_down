
import itertools

def generate_schedule(n, m):
    teams = [f'Team {chr(65+i)}' for i in range(m)]
    players = [f'{team}{j+1}' for team in teams for j in range(n)]
    
    games_per_round = (m-1) * n
    rounds = games_per_round // (m // 2)
    
    pairings = list(itertools.permutations(players, 2))
    
    schedule = []
    for _ in range(rounds):
        games = pairings[:games_per_round]
        pairings = pairings[games_per_round:]
        round_schedule = ' '.join([f'{game[0]}-{game[1]}' for game in games])
        schedule.append(round_schedule)
    
    return schedule

# Input
n, m = map(int, input().split())

# Generate and print the playing schedule
schedule = generate_schedule(n, m)
for round_schedule in schedule:
    print(round_schedule)
