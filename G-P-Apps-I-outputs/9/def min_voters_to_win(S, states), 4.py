
def min_voters_to_win(S, states):
    total_constituents = 0
    total_federals = 0
    total_voters = 0
    total_delegates = 0
    
    for state in states:
        total_constituents += state[1]
        total_federals += state[2]
        total_voters += state[1] + state[2] + state[3]
        total_delegates += state[0]
    
    for state in states:
        constituents_needed = total_constituents // 2 + 1
        federals_needed = total_federals // 2 + 1
        
        if state[1] >= constituents_needed:
            continue
        
        if state[2] >= federals_needed:
            continue
        
        if state[1] + state[2] + state[3] < constituents_needed:
            return "impossible"
            
    return max(0, total_voters - total_constituents)

# Input parsing
S = int(input())
states = []
for _ in range(S):
    D, C, F, U = map(int, input().split())
    states.append((D, C, F, U))

# Call the function with the input
result = min_voters_to_win(S, states)
print(result)
```
