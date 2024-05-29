
def can_match_multiset(N, S):
    S.sort(reverse=True)
    healths = [S[0]]
    for i in range(1, N):
        new_healths = [S[i]] * (2 ** i)
        healths = new_healths + healths + new_healths
    if sorted(healths) == sorted(S):
        return "Yes"
    else:
        return "No"

# Sample Input
N = 2
S = [4, 2, 3, 1]

# Output
print(can_match_multiset(N, S))
```
