
def min_voters_to_convince(S, states):
    total_constituents = total_federals = total_delegates = 0
    for state in states:
        D, C, F, U = state
        total_constituents += C
        total_federals += F
        total_delegates += D

    if total_constituents > total_federals:
        return 0

    required_constituents = (total_delegates + 1) // 2
    remaining_constituents = required_constituents - total_constituents

    if remaining_constituents <= 0:
        return 0

    min_voters_to_convince = 0
    for state in states:
        D, C, F, U = state
        remaining_delegates = (D + 1) // 2
        remaining_voters = remaining_delegates - C

        if remaining_voters < 0:
            return "impossible"
        
        min_voters_to_convince = max(min_voters_to_convince, remaining_voters)

    return min_voters_to_convince

# Input parsing
S = int(input())
states = []
for _ in range(S):
    D, C, F, U = map(int, input().split())
    states.append((D, C, F, U))

# Call the function with the input
result = min_voters_to_convince(S, states)
print(result)
```
