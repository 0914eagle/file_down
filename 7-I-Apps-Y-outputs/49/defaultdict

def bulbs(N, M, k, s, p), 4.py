
from collections import defaultdict

def bulbs(N, M, k, s, p):
    # Write your code here
    d = defaultdict(list)
    for i in range(M):
        d[s[i]].append(i+1)
    res = 0
    for i in range(N):
        if len(d[i+1]) == k[i]:
            res += pow(2, k[i], 1000000007)
    return (res * pow(2, N-M, 1000000007)) % 1000000007

