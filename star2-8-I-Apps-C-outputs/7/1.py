
S = input()
T = [input().split() for _ in range(26)]
K = int(input())
M = int(input())
m = list(map(int, input().split()))
def f(s):
    res = ""
    for c in s:
        res += T[ord(c)-ord('a')]
    return res
def compute_len(s, k):
    if k == 0:
        return len(s)
    elif k == 1:
        return sum(len(x) for x in T)
    else:
        return compute_len(T, k-1)
def solve(s, k, pos):
    if k == 0:
        return s[pos]
    elif k == 1:
        for i, t in enumerate(T):
            if pos < len(t):
                return t[pos]
            else:
                pos -= len(t)
    else:
        return solve(T, k-1, pos)
for i in range(M):
    print(solve(S, K, m[i]-1))

