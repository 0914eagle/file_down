
S = input()

def solve(s):
    if len(s) == 0:
        return 0
    res = 0
    for i in range(len(s)):
        res += int(s[:i+1])
        res += solve(s[i+1:])
    return res

print(solve(S))

