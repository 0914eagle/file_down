
def minimum_voters_to_convince(S, states):
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

    for state in states:
        D, C, F, U = state
        majority_constituents = (total_constituents + U) > total_federals
        majority_federals = (total_federals + U) > total_constituents

        if majority_constituents and not majority_federals:
            remaining_votes_needed = max(0, total_federals - total_constituents)
            return remaining_votes_needed
        elif not majority_constituents and majority_federals:
            remaining_votes_needed = max(0, total_constituents - total_federals)
            return remaining_votes_needed

    return "impossible"

# Input parsing
S = int(input())
states = []
for _ in range(S):
    D, C, F, U = map(int, input().split())
    states.append((D, C, F, U))

# Call the function and print the output
print(minimum_voters_to_convince(S, states))
```
