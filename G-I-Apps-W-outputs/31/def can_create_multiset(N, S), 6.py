
def can_create_multiset(N, S):
    def solve(N, S):
        if N == 1:
            return [S[0]]
        total = sum(S)
        if total % 2 != 0:
            return False
        S1 = solve(N-1, [x for x in S if x <= total // 2])
        if S1 is False:
            return False
        x = total // 2 - S1[0]
        if x <= 0:
            return False
        return [x] + S1 + [x] * (2**(N-1) - 1)

    result = solve(N, S)
    if result is False:
        return "No"
    return "Yes"

# Sample Input
N = 2
S = [4, 2, 3, 1]
print(can_create_multiset(N, S))
```
