
def is_consistent_championship(N, M, matches):
    skills = [0] * N
    for match in matches:
        player1, outcome, player2 = match
        if outcome == '=':
            if skills[player1] != skills[player2]:
                return "inconsistent"
        elif outcome == '>':
            skills[player1] = max(skills[player1], skills[player2] + 1)
        else:
            skills[player2] = max(skills[player2], skills[player1] + 1)
    
    return "consistent"

# Read input
N, M = map(int, input().split())
matches = []
for _ in range(M):
    match = input().split()
    player1, outcome, player2 = int(match[0]), match[1], int(match[2])
    matches.append((player1, outcome, player2))

# Check consistency
result = is_consistent_championship(N, M, matches)
print(result)
```
