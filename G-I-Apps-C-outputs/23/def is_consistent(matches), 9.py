
def is_consistent(matches):
    n = len(matches)
    ranking = [-1] * n  # Initialize player rankings
    
    for match in matches:
        player1, result, player2 = match
        if result == '=':
            if ranking[player1] == -1 and ranking[player2] == -1:
                ranking[player1] = 0
                ranking[player2] = 0
            elif ranking[player1] != ranking[player2]:
                return "inconsistent"
        elif result == '>':
            if ranking[player1] == -1 and ranking[player2] == -1:
                ranking[player1] = 1
                ranking[player2] = 0
            elif ranking[player1] == -1 and ranking[player2] == 1:
                ranking[player1] = 1
            elif ranking[player1] == 0 and ranking[player2] == 0:
                ranking[player1] = 1
            elif ranking[player1] == 1 and ranking[player2] == 0:
                continue
            else:
                return "inconsistent"
    
    return "consistent"

# Read input
N, M = map(int, input().split())
matches = []
for _ in range(M):
    K, result, L = input().split()
    matches.append((int(K), result, int(L)))

# Check consistency
result = is_consistent(matches)
print(result)
```
