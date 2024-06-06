
from collections import defaultdict

def solve(s, words):
    n = len(s)
    dp = defaultdict(list)
    dp[0].append([])
    for i in range(n):
        for j in range(i, n):
            if s[i:j+1] in words:
                for k in dp[i]:
                    dp[j+1].append(k + [s[i:j+1]])
    if dp[n] == []:
        return "impossible"
    elif len(dp[n]) > 1:
        return "ambiguous"
    else:
        return " ".join(dp[n][0])

s = input()
n = int(input())
words = [input() for _ in range(n)]
print(solve(s, words))
