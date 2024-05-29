
def is_consistent(matches):
    wins = {}
    for match in matches:
        player1, result, player2 = match
        if result == '=':
            if wins.get(player1, None) == wins.get(player2, None):
                continue
            else:
                return "inconsistent"
        elif result == '>':
            if wins.get(player1, None) is not None and wins.get(player2, None) is not None:
                if wins[player1] > wins[player2]:
                    continue
                else:
                    return "inconsistent"
            elif wins.get(player1, None) is None and wins.get(player2, None) is not None:
                wins[player1] = wins[player2] + 1
            elif wins.get(player1, None) is not None and wins.get(player2, None) is None:
                wins[player2] = wins[player1] - 1
            else:  # Both players' skills unknown
                wins[player1] = 1
                wins[player2] = 0

    return "consistent"

# Input parsing
N, M = map(int, input().split())
reported_matches = []
for _ in range(M):
    k, result, L = input().split()
    reported_matches.append((int(k), result, int(L)))

# Check consistency
result = is_consistent(reported_matches)
print(result)
```
