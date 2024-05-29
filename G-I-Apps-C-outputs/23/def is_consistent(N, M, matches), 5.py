
def is_consistent(N, M, matches):
    skill_levels = [0] * N  # Initialize skill levels for all players
    
    for match in matches:
        player1, result, player2 = match
        if result == '=':
            if skill_levels[player1] != skill_levels[player2]:
                return "inconsistent"
        elif result == '>':
            if skill_levels[player1] <= skill_levels[player2]:
                return "inconsistent"
            else:
                skill_levels[player1] = max(skill_levels[player1], skill_levels[player2] + 1)
    
    return "consistent"

# Input processing
N, M = map(int, input().split())
matches = [tuple(input().split()) for _ in range(M)]

# Convert player IDs to integers for easier processing
player_dict = {}
id_count = 0
for match in matches:
    player1, _, player2 = match
    if player1 not in player_dict:
        player_dict[player1] = id_count
        id_count += 1
    if player2 not in player_dict:
        player_dict[player2] = id_count
        id_count += 1
    match = (player_dict[player1], match[1], player_dict[player2])

result = is_consistent(N, M, matches)
print(result)
```
