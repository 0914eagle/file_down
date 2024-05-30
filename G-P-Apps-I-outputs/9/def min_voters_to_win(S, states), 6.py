
def min_voters_to_win(S, states):
    min_voters = 0
    total_constituents = 0
    total_federals = 0
    total_undecided = 0
    
    for state in states:
        D, C, F, U = state
        total_constituents += C
        total_federals += F
        total_undecided += U
        majority = (C + F) // 2 + 1
        if C > F + U:  # Already won by Constituents
            continue
        elif F > C + U:  # Already won by Federals
            min_voters += U
        else:
            min_voters += max(0, majority - C)
    
    if total_constituents > total_federals + total_undecided:
        return min_voters
    else:
        return "impossible"

# Input parsing
S = int(input())
states = []
for _ in range(S):
    D, C, F, U = map(int, input().split())
    states.append((D, C, F, U))

# Call the function and output the result
result = min_voters_to_win(S, states)
print(result)
```
