
def min_voters_to_win(S, states):
    total_constituents = 0
    total_federals = 0
    total_delegates = 0

    for state in states:
        D, C, F, U = state
        total_constituents += C
        total_federals += F
        total_delegates += D

    # Check if it is impossible to win
    if total_constituents > total_federals + total_delegates // 2:
        return "impossible"

    min_voters_to_win = max(0, (total_federals + total_delegates // 2 + 1) - total_constituents)

    return min_voters_to_win

# Input parsing
S = int(input())
states = []
for _ in range(S):
    D, C, F, U = map(int, input().split())
    states.append((D, C, F, U))

# Call the function and print the result
result = min_voters_to_win(S, states)
print(result)
```
