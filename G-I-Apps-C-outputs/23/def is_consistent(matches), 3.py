
def is_consistent(matches):
    rankings = [0] * N
  
    for match in matches:
        k, symbol, l = match
        if symbol == '=':
            if rankings[k] != rankings[l]:
                return "inconsistent"
        elif symbol == '>':
            if rankings[k] <= rankings[l]:
                rankings[k] = max(rankings[k], rankings[l] + 1)
            else:
                return "inconsistent"
    
    return "consistent"

# Reading input
N, M = map(int, input().split())
matches = []

for _ in range(M):
    K, symbol, L = input().split()
    K, L = int(K), int(L)
    matches.append((K, symbol, L))

# Checking consistency
result = is_consistent(matches)
print(result)
```
