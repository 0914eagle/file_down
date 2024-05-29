
def is_consistent(N, M, matches):
    skill_levels = [0] * N
    
    for i in range(M):
        K, symbol, L = matches[i]
        if symbol == '>':
            if skill_levels[K] <= skill_levels[L]:
                return "inconsistent"
            skill_levels[K] = max(skill_levels[K], skill_levels[L] + 1)
        elif symbol == '=':
            if skill_levels[K] != skill_levels[L]:
                return "inconsistent"
    
    return "consistent"

# Input parsing
N, M = map(int, input().split())
matches = []
for _ in range(M):
    K, symbol, L = input().strip().split()
    matches.append((int(K), symbol, int(L)))

# Check consistency
result = is_consistent(N, M, matches)
print(result)
```
