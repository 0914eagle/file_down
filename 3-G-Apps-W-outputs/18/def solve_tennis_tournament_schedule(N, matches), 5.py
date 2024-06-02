
def solve_tennis_tournament_schedule(N, matches):
    schedule = []
    days = 0
    while len(schedule) < N*(N-1)//2:
        day_matches = set()
        for i in range(N):
            if len(matches[i]) == 0:
                continue
            opponent = matches[i].pop(0)
            if (i, opponent) in day_matches or (opponent, i) in day_matches:
                return -1
            day_matches.add((i, opponent))
        schedule.append(day_matches)
        days += 1
    return days

# Reading input
N = int(input())
matches = []
for _ in range(N):
    matches.append(list(map(int, input().split())))

# Calling the function and printing the result
result = solve_tennis_tournament_schedule(N, matches)
print(result)
