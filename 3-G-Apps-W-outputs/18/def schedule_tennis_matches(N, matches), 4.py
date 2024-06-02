
def schedule_tennis_matches(N, matches):
    schedule = []
    days = 0
    while len(schedule) < N*(N-1)//2:
        played_today = set()
        for i in range(N):
            if i in played_today:
                continue
            opponent = matches[i][0]
            if opponent in played_today:
                return -1
            if matches[opponent-1][0] != i+1:
                return -1
            played_today.add(i)
            played_today.add(opponent-1)
            schedule.append((i+1, opponent))
        days += 1
    return days

# Input
N = int(input())
matches = [list(map(int, input().split())) for _ in range(N)]

# Output
result = schedule_tennis_matches(N, matches)
print(result)
