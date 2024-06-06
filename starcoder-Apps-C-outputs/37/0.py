
# 18.08.25.py

import sys

def go(n, m, lines):
    dp = [[None] * (n+1) for i in range(m+1)]
    path = [[None] * (n+1) for i in range(m+1)]

    def _go(i, t):
        if dp[i][t] is not None:
            return dp[i][t]
        if i == m:
            if t == n:
                return 0
            else:
                return -1
        ans = -1
        for dt in [-1, 0, 1]:
            tmp = _go(i+1, t+1)
            if tmp != -1:
                tmp += 1
                if ans == -1 or ans > tmp:
                    ans = tmp
                    path[i][t] = dt
        dp[i][t] = ans
        return ans
    if _go(0, 0) == -1:
        return 'impossible'
    else:
        ans = []
        i, t = 0, 0
        while True:
            ans.append({-1:'-', 0:'0', 1:'+'}.get(path[i][t]))
            if i == m:
                return ''.join(ans)
            i += 1
            t += 1

if __name__ == '__main__':
    n, m = map(int, input().split())
    lines = [input().split() for _ in range(m)]
    print(go(n, m, lines))
