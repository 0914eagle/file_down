
def schedule_tennis_matches(N, matches):
    schedule = []
    days = 0
    while len(schedule) < N*(N-1)//2:
        day_matches = set()
        for i in range(N):
            if i not in day_matches:
                opponent = matches[i][0]
                if opponent not in day_matches:
                    day_matches.add(i)
                    day_matches.add(opponent-1)
                    schedule.append((i+1, opponent))
        if len(day_matches) == 0:
            return -1
        days += 1
    return days

# Input parsing
N = int(input())
matches = []
for _ in range(N):
    matches.append(list(map(int, input().split())))

result = schedule_tennis_matches(N, matches)
print(result)
