
def is_consistent(N, M, matches):
    ranking = [0] * N
    
    for match in matches:
        player1, result, player2 = match
        if result == '=':
            if ranking[player1] != ranking[player2]:
                return "inconsistent"
        elif result == '>':
            if ranking[player1] <= ranking[player2]:
                ranking[player1] = max(ranking[player1], ranking[player2] + 1)
            else:
                return "inconsistent"
    
    return "consistent"


# Reading input
N, M = map(int, input().split())
matches = []
for _ in range(M):
    K, result, L = input().split()
    K, L = int(K), int(L)
    matches.append((K, result, L))

# Checking consistency
result = is_consistent(N, M, matches)
print(result)
```
