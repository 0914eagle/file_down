
def solve(S):
    if S[0] == 'a' and S[1] == 'b' and S[2] == 'c':
        return 'Yes'
    elif S[0] == 'b' and S[1] == 'a' and S[2] == 'c':
        return 'Yes'
    elif S[0] == 'b' and S[1] == 'c' and S[2] == 'a':
        return 'Yes'
    elif S[0] == 'c' and S[1] == 'a' and S[2] == 'b':
        return 'Yes'
    elif S[0] == 'c' and S[1] == 'b' and S[2] == 'a':
        return 'Yes'
    elif S[0] == 'a' and S[1] == 'c' and S[2] == 'b':
        return 'Yes'
    else:
        return 'No'

S = input()
print(solve(S))

