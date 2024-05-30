
def min_voters_needed(S, states):
    total_con = 0
    total_fed = 0
    total_undecided = 0
    total_delegates = 0
    
    for state in states:
        D, C, F, U = state
        total_delegates += D
        total_con += C
        total_fed += F
        total_undecided += U
    
    if total_con + total_fed > total_delegates // 2:
        return 0
    
    remaining_delegates = total_delegates - total_con - total_fed
    remaining_undecided = total_undecided - remaining_delegates
    if remaining_undecided < 0 or total_con > total_fed + remaining_undecided:
        return "impossible"
    
    return total_fed + remaining_undecided - total_con

# Input processing
S = int(input())
states = []
for _ in range(S):
    D, C, F, U = map(int, input().split())
    states.append((D, C, F, U))

# Output the result
result = min_voters_needed(S, states)
print(result)
```
