
def solve_tennis_tournament(N, matches):
    schedule = []
    for i in range(N):
        played = set()
        day = 0
        while len(played) < N - 1:
            day += 1
            new_matches = []
            for j in range(N-1):
                if matches[i][j] not in played and matches[matches[i][j]-1][j] not in played:
                    new_matches.append((i+1, matches[i][j]))
                    played.add(matches[i][j])
                    played.add(matches[matches[i][j]-1][j])
            if not new_matches:
                return -1
            schedule.append(new_matches)
    return day

# Input processing
N = int(input())
matches = []
for _ in range(N):
    matches.append(list(map(int, input().split())))

# Call the function and print the result
result = solve_tennis_tournament(N, matches)
print(result)
