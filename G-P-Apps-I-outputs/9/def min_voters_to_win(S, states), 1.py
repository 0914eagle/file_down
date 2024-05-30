
def min_voters_to_win(S, states):
    total_constituents = 0
    total_federals = 0
    total_undecided = 0
    total_delegates = 0
    
    for state in states:
        D, C, F, U = state
        total_constituents += C
        total_federals += F
        total_undecided += U
        total_delegates += D
    
    if total_constituents > total_federals:  # If Constituents are already leading in total voters, victory is guaranteed
        return 0
    
    remaining_delegates_needed = (total_delegates // 2) + 1 - total_constituents  # Minimum delegates needed to win
    remaining_voters_needed = remaining_delegates_needed - total_undecided
    
    if remaining_voters_needed <= 0:
        return 0
    elif remaining_voters_needed <= total_undecided:
        return remaining_voters_needed
    else:
        return "impossible"

# Input parsing
S = int(input())
states = []
for _ in range(S):
    D, C, F, U = map(int, input().split())
    states.append((D, C, F, U))

# Output
result = min_voters_to_win(S, states)
print(result)
```
