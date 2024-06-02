
def schedule_tennis_matches(N, matches):
    schedule = []
    for i in range(N-1):
        day_matches = set()
        for j in range(N):
            player1 = j + 1
            player2 = matches[j][i]
            if (player1, player2) in day_matches or (player2, player1) in day_matches:
                return -1
            day_matches.add((player1, player2))
        schedule.append(day_matches)
    
    return len(schedule)

# Sample Input Parsing
N = 3
matches = [
    [2, 3],
    [1, 3],
    [1, 2]
]

# Call the function with the sample input
result = schedule_tennis_matches(N, matches)
print(result)
