
def solve_tennis_tournament(N, matches):
    schedule = []
    for day in range(N):
        played = set()
        for player in range(N):
            if player in played:
                continue
            opponent = matches[player][0]
            if player == matches[opponent - 1][0] and opponent not in played:
                schedule.append((player + 1, opponent))
                played.add(player)
                played.add(opponent - 1)
            else:
                return -1
    return len(schedule)

# Read input
N = int(input())
matches = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the result
result = solve_tennis_tournament(N, matches)
print(result)
