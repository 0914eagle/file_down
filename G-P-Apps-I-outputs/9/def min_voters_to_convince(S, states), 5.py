
def min_voters_to_convince(S, states):
    total_delegates = sum(state[0] for state in states)
    total_constituents = sum(state[1] for state in states)
    total_federals = sum(state[2] for state in states)

    min_voters_needed = 0
    for state in states:
        d, c, f, u = state
        if c > f + u:  # Constituents already have majority
            continue
        if f > c + u:  # Federals already have majority
            min_voters_needed += u
        else:  # Need to convince undecided voters
            needed_for_majority = (f + u + 1) - c
            min_voters_needed += max(0, needed_for_majority)

    if total_constituents + min_voters_needed <= total_federals:  # Impossible to secure a victory
        return "impossible"
    else:
        return min_voters_needed

# Input processing
S = int(input())
states = [list(map(int, input().split())) for _ in range(S)]

# Output
print(min_voters_to_convince(S, states))
```
