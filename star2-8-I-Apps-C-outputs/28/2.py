
def solve(s):
    res = 0
    n = len(s)
    for i in range(n):
        if s[i] == '1':
            res = max(res, i+1)
    return res

