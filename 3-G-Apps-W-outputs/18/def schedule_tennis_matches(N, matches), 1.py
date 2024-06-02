
def schedule_tennis_matches(N, matches):
    schedule = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N-1):
            schedule[i][matches[i][j]-1] = j + 1
    
    days = 0
    for _ in range(N):
        played = [False] * N
        matches_left = N
        for i in range(N):
            if not played[i]:
                matches_left -= 1
                played[i] = True
                opponent = schedule[i].index(matches[i][0])
                played[opponent] = True
                for j in range(1, N-1):
                    if not played[matches[i][j]-1]:
                        played[matches[i][j]-1] = True
                        opponent = schedule[matches[i][j]-1].index(i+1)
                        played[opponent] = True
                        matches_left -= 1
                if matches_left == 0:
                    days += 1
                    break
    if days == N:
        return days
    else:
        return -1

# Sample Input
N = 3
matches = [[2, 3], [1, 3], [1, 2]]

# Output
result = schedule_tennis_matches(N, matches)
print(result)
