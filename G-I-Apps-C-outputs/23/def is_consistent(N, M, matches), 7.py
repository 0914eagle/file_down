
def is_consistent(N, M, matches):
    skill_levels = [0] * N
    
    for i in range(M):
        player1, result, player2 = matches[i]
        
        if result == '=':
            if skill_levels[player1] != skill_levels[player2]:
                return "inconsistent"
        elif result == '>':
            if skill_levels[player1] <= skill_levels[player2]:
                return "inconsistent"
            skill_levels[player1] = max(skill_levels[player1], skill_levels[player2] + 1)
        else:
            return "inconsistent"
    
    return "consistent"

# Input handling
N, M = map(int, input().split())
matches = []
for _ in range(M):
    K, result, L = input().split()
    K, L = int(K), int(L)
    matches.append((K, result, L))

# Check consistency
result = is_consistent(N, M, matches)

# Output result
print(result)
