
def min_voters_to_convince(S, states):
    total_constituents = 0
    total_federals = 0
    total_undecided = 0
    total_delegates = 0

    for state in states:
        D, C, F, U = state
        total_delegates += D
        total_constituents += C
        total_federals += F
        total_undecided += U

    if total_constituents + total_undecided > total_federals:
        return total_constituents + total_undecided - total_federals
    else:
        return "impossible"

# Input processing
S = int(input())
states = []
for _ in range(S):
    D, C, F, U = map(int, input().split())
    states.append((D, C, F, U))

# Call the function and print the result
result = min_voters_to_convince(S, states)
print(result)
```
