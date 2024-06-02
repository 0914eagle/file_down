
def solve(S):
    if S[2] == S[3] and S[4] == S[5]:
        return "Yes"
    else:
        return "No"

S = input()
print(solve(S))

