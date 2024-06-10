
S = input()
T = [input().split() for _ in range(26)]
K = int(input())
M = int(input())
m = list(map(int, input().split()))
S_len = len(S)
T_len = [len(t) for t in T]
f_len = sum(T_len)
f = [[] for _ in range(f_len)]
f_idx = 0
for i in range(26):
    for j in range(T_len[i]):
        f[f_idx] = T[i][j]
        f_idx += 1
def f_K(S, K):
    res = ""
    for _ in range(K):
        res += S
    return res
def get_m(m, S_len, f_len, f_idx):
    res = ""
    for idx, i in enumerate(m):
        if i <= S_len:
            res += S[i-1]
        else:
            i -= S_len
            while i > f_len:
                i -= f_len
            res += f[i-1]
    return res
print(get_m(m, S_len, f_len, f_idx))

