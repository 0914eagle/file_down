
#hackerrank
import sys

def solve(s, t):
    # Complete this function
    ans = s[0] + t[0]
    if (len(s) > 1):
        if (len(t) > 1):
            ans = min(ans, s[0] + t[0], s[0] + t[1], s[1] + t[0])
        else:
            ans = min(ans, s[0] + t[0])
    else:
        if (len(t) > 1):
            ans = min(ans, s[0] + t[0], s[0] + t[1])
        else:
            ans = min(ans, s[0] + t[0])
    return ans

s, t = raw_input().strip().split(' ')
s, t = [str(s), str(t)]
result = solve(s, t)
print(result)
