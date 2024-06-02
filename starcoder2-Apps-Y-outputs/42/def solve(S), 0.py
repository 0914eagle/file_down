
def solve(S):
    return "Yes" if S == "abc" or S == "acb" or S == "bac" or S == "bca" or S == "cab" or S == "cba" else "No"

S = input()
print(solve(S))

