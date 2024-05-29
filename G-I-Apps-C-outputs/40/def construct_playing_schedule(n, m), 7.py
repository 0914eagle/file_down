
def construct_playing_schedule(n, m):
    teams = [chr(65 + i) for i in range(m)]  # Teams denoted by capital letters A, B, C, ...
    players = [f"{team}{j}" for team in teams for j in range(1, n + 1)]  # Players denoted by team letter and player number

    total_rounds = (m - 1) * n + 1
    games_per_round = m * n // 2

    for i in range(total_rounds):
        round_schedule = []
        for j in range(games_per_round):
            p1 = players[(i + j) % (m * n)]
            p2 = players[(i + m * n - j) % (m * n)]
            round_schedule.append(f"{p1}-{p2}")
        print(" ".join(round_schedule))

# Read input values
n, m = map(int, input().split())

# Call the function with the input values
construct_playing_schedule(n, m)
