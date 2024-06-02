
def solve(S):
    n = len(S)
    if n == 1:
        return 0
    if S[0] == S[-1]:
        return 1
    else:
        return 0

S = input()
print(solve(S))

