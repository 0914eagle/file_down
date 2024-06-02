
def schedule_tennis_matches(N, matches):
    schedule = []
    days = 0
    while len(schedule) < N*(N-1)//2:
        day_matches = set()
        for i in range(N):
            if i in day_matches:
                continue
            opponent = matches[i][0]
            if opponent in day_matches:
                return -1
            if matches[opponent-1][0] != i+1:
                return -1
            day_matches.add(i)
            day_matches.add(opponent-1)
            schedule.append((i+1, opponent))
        days += 1
    return days

# Input parsing
N = int(input())
matches = []
for _ in range(N):
    matches.append(list(map(int, input().split())))

result = schedule_tennis_matches(N, matches)
print(result)
