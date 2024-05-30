
def minimum_voters_to_win(S, states):
    total_constituents = 0
    total_federals = 0
    total_undecided = 0

    for state in states:
        D, C, F, U = state
        total_constituents += C
        total_federals += F
        total_undecided += U

        if C > F + U:
            total_constituents -= C - F - U
        elif F > C + U:
            total_federals -= F - C - U

    if total_constituents > total_federals:
        return 0
    elif total_constituents + total_undecided <= total_federals:
        return "impossible"
    else:
        return total_federals - total_constituents + 1

# Input
S = int(input())
states = []
for _ in range(S):
    D, C, F, U = map(int, input().split())
    states.append((D, C, F, U))

# Output
print(minimum_voters_to_win(S, states))
```
